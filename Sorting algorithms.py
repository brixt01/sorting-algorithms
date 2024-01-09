import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()
import random
import time

# Create initial list
def makeList():
    initialList = [i for i in range(1, numberOfBars+1)]
    finalList = []
    while initialList != []:
        randomIndex = random.randint(0, len(initialList)-1)
        finalList.append(initialList[randomIndex])
        initialList.pop(randomIndex)
    return finalList

# Updating graphics
def updateGraphics():
    window.fill((0, 0, 0))
    for item in list:
        x = list.index(item) * screenWidth/len(list)
        y = screenHeight - (screenHeight/len(list)) * list[list.index(item)]
        width = screenWidth/len(list)
        height = (screenHeight/len(list)) * list[list.index(item)]
        pygame.draw.rect(window, (200, 0, 0), (x, y, width, height))
    pygame.display.update()

# Main
while(True):
    try:
        numberOfBars = int(input("How many bars?:\n"))
    except:
        print("Please enter an integer.\n")
    if numberOfBars >= 10:
        algorithmChoice = input("\nWhich algorithm?:\n- Bubble sort (bubble)\n- Selection sort (select)\n")
        if algorithmChoice == "bubble" or algorithmChoice == "select":
            break
        else:
            print("Please choose one of the given choices.\n")
    else:
        print("Values must be at least 10.\n")

pygame.display.set_caption("Sorting algorithm visualiser")
screenWidth = 854
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))
list = makeList()
updateGraphics()

if algorithmChoice == "bubble":
    tempList = list.copy()
    startTime = time.perf_counter()
    counter = 0
    while counter < len(tempList)-1:
        pygame.event.get()
        if tempList[counter] > tempList[counter+1]:
            tempList[counter], tempList[counter+1] = tempList[counter+1], tempList[counter]
            counter = 0
        else:
            counter += 1
    endTime = time.perf_counter()

    counter = 0
    while counter < len(tempList)-1:
        pygame.event.get()
        if list[counter] > list[counter+1]:
            list[counter], list[counter+1] = list[counter+1], list[counter]
            counter = 0
            updateGraphics()
            time.sleep(10/numberOfBars)
        else:
            counter += 1
    timeTaken = round((endTime - startTime), 3)
    print(f"\nThis would have taken the computer {timeTaken} seconds to complete this operation.")

elif algorithmChoice == "select":
    tempList = list.copy()
    startTime = time.perf_counter()
    startValue = 0
    while startValue < len(tempList):
        counter = startValue+1
        current = tempList[startValue]
        while counter < len(tempList):
            pygame.event.get()
            if tempList[counter] < current:
                current = tempList[counter]
            else:
                counter += 1
        tempList.insert(startValue, tempList.pop(tempList.index(current)))
        startValue += 1
    endTime = time.perf_counter()

    startValue = 0
    while startValue < len(list):
        counter = startValue+1
        current = list[startValue]
        while counter < len(list):
            pygame.event.get()
            if list[counter] < current:
                current = list[counter]
            else:
                counter += 1
        list.insert(startValue, list.pop(list.index(current)))
        startValue += 1
        updateGraphics()
        time.sleep(10/numberOfBars)
    timeTaken = round((endTime - startTime), 3)
    print(f"\nThis would have taken the computer {timeTaken} seconds to complete this operation.")
