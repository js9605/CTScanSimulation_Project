import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import math

# square matrix only
class Computer_tomography:

    def __init__(self):
        self.filename  = "graphic_for_testing.jpg"
        self.img = misc.imread(self.filename)

    def up(self):
        rays_detected = []
        for col in range(len(self.img[0])):
            index = 0
            for row in range(len(self.img)):
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)
        return rays_detected[:]

    def left(self):
        rays_detected = []
        for row in range(len(self.img)):
            index = 0
            for col in range(len(self.img[row])):
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)

        return rays_detected[:]

    # ray goes from top left corner
    def TopLeft(self):
        rays_detected = []

        for col in range(len(self.img) - 1, -1, -1):
            index = 0
            for row in range((len(self.img)-1) - col):    # 10 - 1 - [9,8,7]
                col += 1
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)

        #diagonal
        index = 0
        for row in range(len(self.img)):
            if sum(self.img[row][row]) <= 50:
                index += 1
        rays_detected.append(index)

        for row in range(len(self.img) - 1, -1, -1):  # [9 8 7 ]
            index = 0
            for col in range((len(self.img)-1) - row):    # 10 - 1 - [9,8,7]     [0,1,2]
                row += 1
                if sum(self.img[row][col]) <= 50:
                    index += 1

        for row in range(len(self.img)):
            index = 0
            for col in range((len(self.img)-1) - row):
                row += 1
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)

        del rays_detected[0]
        del rays_detected[-1]
        return rays_detected[:]

    def TopRight(self):
        list = []
        tsil = []

        for i in range(len(self.img)):
            list.append(i)

        for i in range(len(self.img)):
            tsil.append(list[-i])

        rays_detected = []
        row = 0
        for col in list:
            index = 0
            for j in range(col + 1):
                # print(row + j,col - j)
                if sum(self.img[row + j][col - j]) <= 50:
                    index += 1
            rays_detected.append(index)
        return rays_detected



ct = Computer_tomography()
memory = ct.TopRight()
print(memory)



