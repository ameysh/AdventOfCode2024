# Advent of Code 2024: Day 1

list1, list2 = [], []
totalDistance = 0

with open('input.txt', 'r') as file:
    for line in file:
        column1, column2 = map(int, line.strip().split())
        list1.append(column1)
        list2.append(column2)

list1 = sorted(list1)
list2 = sorted(list2)

for element1, element2 in zip(list1, list2):
    totalDistance += abs(element1 - element2)

print(totalDistance)