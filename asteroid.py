import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)

    def update(self, dt):
        self.position+= self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            left_angle = self.velocity.rotate(angle)
            right_angle =  self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            roid1 =Asteroid(self.position[0], self.position[1], new_radius)
            roid1.velocity = left_angle *1.2
            roid2 =Asteroid(self.position[0], self.position[1], new_radius)
            roid2.velocity = right_angle *1.2
