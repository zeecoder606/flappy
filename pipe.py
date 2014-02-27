#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

head = pygame.image.load('head_pipe.png')
body = pygame.image.load('pipe.png')


class Pipe(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, height=82):
        pygame.sprite.Sprite.__init__(self)

        self.mPos = [x, y]
        self.mVel = -5
        if height < 82:
            height = 82
        h = height - 42
        self.p = h / 40
        self.height = self.p * 40 + 42
        self.image = pygame.surface.Surface((91, self.height), 0)
        self.image.fill((255, 255, 255))
        
        self.image.blit(head, (0, 0))
        for i in range(self.p):
            self.image.blit(body, (4, 42 + i * 40))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
 
    def setXY(self, aX, aY):
        self.mPos = [aX, aY]

    def setPosTuple(self, position):
        self.mPos = position

    def setVel(self, aVec):
        self.mVel = aVec

    def update(self):
        self.mPos[0] = self.mPos[0] + self.mVel
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]
        
    def getX(self):
        return self.mPos[0]
    
    def getY(self):
        return self.mPos[1]
   
    def getSize(self):
        return (self.rect[2], self.rect[3])

    def destroy(self):
        self.image = None

