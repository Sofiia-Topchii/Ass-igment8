import pgzrun
import pygame as pg


WIDTH = 600
HEIGHT = 800

pg.init()

# Create a Paddle class for the moving platform at the bottom of the screen
class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        # Draw the paddle as a rectangle
        pg.draw.rect(pg.display.get_surface(), (255, 255, 255), (self.x, self.y, self.width, self.height))

    def update(self):
        # Update the paddle's position based on mouse movement
        self.x = pg.mouse.get_pos()[0]

# Create a Ball class for the ball that moves and bounces off walls
class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        # Draw the ball as a circle
        pg.draw.circle(pg.display.get_surface(), (255, 255, 255), (self.x, self.y), self.radius)

    def update(self):
        # Update the ball's position based on its speed
        self.x += self.speed_x * 3
        self.y += self.speed_y * 3
                # Check if the ball hits a wall and reverse its direction accordingly
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y - self.radius <= 0:
            self.speed_y *= -1

# Create an Obstacle class for the obstacles on the game field
class Obstacle:
    def __init__(self, x, y, width, height, hits):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hits = hits

    def draw(self):
        if self.hits == 3:
            color = (255, 0, 0)
        elif self.hits == 2:
            color = (255, 255, 0)
        else:
            color = (255, 255, 255)
        pg.draw.rect(pg.display.get_surface(), color, (self.x, self.y, self.width, self.height))

