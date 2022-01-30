#print('Hello World')

import numpy as np
import ast
from ctypes import pointer
import csv



#Up to 1000 
points = 0

def medicalSeverity(medSevere):
    global points
    #Medical Severity (0 to 10)
    if(medSevere == 0):
        points += 200
    elif(medSevere == 1):
        points += 200
    elif(medSevere == 2):
        points += 150
    elif(medSevere == 3):
        points += 125
    elif(medSevere == 4):
        points += 100
    elif(medSevere == 5):
        points += 75
    elif(medSevere >= 6):
        points += 0

def prescriptionSeverity(presSev):
    global points
    if(presSev == 0):
        points += 100
    elif(presSev > 0 & presSev <= 3):
        points += 50
    elif(presSev > 3):
        points += 0


def smoker(smoke):
    global points
    #will read in data from input file
    if(smoke == 'No'):
        points += 100
    elif(smoke == 'Yes'):
        points += 0

def drugUse(use):
    global points
    #will read in data from input file
    if(use == 0):
        points += 100
    else:
        points += 0

def exercise():
    #bruh
    print('To be worked on.')


def drinkUse():
    global points
    #will read in data from input files
    #scale from 0 to 3 based on drinking usage
    # 1 - barely drink if not at all
    # 2 - sometimes drink
    # 3 - recreational drinker (3 or more times a week)
    drinkSev = 0

    if(drinkSev == 1):
        points += 50
    elif(drinkSev == 2):
        points += 25
    elif(drinkSev == 3):
        points += 0


def jobType():
    global points
    #will most likely need to be coupled with exercise and age later
    job = 'Unemployed'
    if(job == 'Unemployed'):
        points += 0
    elif(job == 'Indoors'):
        points += 100
    elif(job == 'Outdoors'):
        points += 100

def drivingRecord():
    global points
    #will read in data from input file
    drivingScale = 0

    if(drivingScale == 0):
        points += 100
    elif(drivingScale >= 1):
        points += 0

def criminalRecord():
    print()


def weight():
    print()

def familyConditions():
    print()

def gender():
    print()

def age():
    print()

def hobbies():
    print()

def insuranceType():
    #this will be separate from the point scale
    #long term will have a lower discount than short term as a base factor
    print()

with open('input.csv', mode = 'rt') as file:
    csvreader = csv.reader(file)
    line_count = 0
    for row in csvreader:
        if(line_count == 0):
            print(f'Records are shown as: {", ".join(row)}')
            line_count += 1
        else:
            print('Name:', row[0])
            smoker(row[1])
            medicalSeverity(int(row[2]))
            drugUse(row[3])
            prescriptionSeverity(int(row[4]))
            line_count += 1
    #print('Completed read through input.txt')
        #print(1)

if(points > 100):
    eligible = True
if(eligible == True):
    print("Eligible for discount: Yes")
else:
    print("Eligible for discount: No")

print("Points are:", points)