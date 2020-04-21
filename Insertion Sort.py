import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Insertion Sort")


# Draws the current array, updates color every time its called
def draw(n, j):
    count = 0  # For the Spacing of lines
    screen.fill((0, 0, 0))
    for i in range(1, len(array)):
        if i == n:  # Draws green on the current item
            pygame.draw.line(screen, (0, 255, 0), (i + count, 500), (i + count, 500 - array[i]), 7)
        elif i == j or i == j + 1:  # Draws red on the current items being swapped
            pygame.draw.line(screen, (255, 0, 0), (i + count, 500), (i + count, 500 - array[i]), 7)
            pygame.draw.line(screen, (255, 0, 0), (i + count + 9, 500), (i + count + 9, 500 - array[i + 1]), 7)
        else:  # Draws a regular white line
            pygame.draw.line(screen, (255, 255, 255), (i + count, 500), (i + count, 500 - array[i]), 7)
        count += 8  # For spacing of lines
    pygame.display.update()


# Starts algorithm
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            draw(i, j)  # Draws array after each change
            pygame.time.wait(50)
        arr[j + 1] = key
    draw(-1, -1)  # Draws the completed array once sorted


array = []
for i in range(0, 57):  # Randomizes array with 50 values
    array.append(random.randint(25, 200))

insertionSort(array)
spacing = 0  # Allows each line to be separated
for i in range(1, len(array)):  # Does end of sort graphic
    pygame.draw.line(screen, (0, 255, 0), (i + spacing, 500), (i + spacing, 500 - array[i]), 7)
    pygame.display.update()
    pygame.time.wait(25)
    spacing += 8
