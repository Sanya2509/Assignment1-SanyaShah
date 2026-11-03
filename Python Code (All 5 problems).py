# Python Code (All 5 problems)

#Problem 1 : Cyclic Rotation
def solution(A,K):
    #Repeat the rotation K times
    for i in range(K):
        #Save the last element
        last_element=A[-1]
        #Move the last element to the beginning
        A=[last_element]+A[:-1]
    # Return the rotated array
    return A

#Problem 2 : Perm Missing Element
def solution(A):
    #Find the number of elements in the array
    N=len(A)
    #Check every number from 1 to N + 1
    for i in range(1,N+2):
        # If the number is not in A, it is the missing number
        if i not in A:
            return i

#Problem 3 : Passing Cars
def solution(A):
    #Count the number of eastbound cars
    east=0
    #Count the total number of passing pairs
    passing=0
    #Go through each car in the array
    for car in A:
        #If the car is going east
        if car==0:
            east+=1
        #If the car is going west
        else:
            passing+=east
    #Return -1 if there are more than 1000000000 pairs
    if passing>1000000000:
        return -1
    #Return the total number of passing pairs

#Problem 4 : Odd Occurences in an Array 
def solution(A):
    #Create an empty dictionary
    numbers = {}
    #Go through each number in the array
    for number in A:
        #If the number is already in the dictionary
        if number in numbers:
            #Change its value from True to False or False to True
            numbers[number] = not numbers[number]
        else:
            #Add the number with a value of True
            numbers[number] = True
    #Go through the dictionary
    for number in numbers:
        #Find the number that appears an odd number of times
        if numbers[number]:
            return number


#Problem 5 : Frog River One 
def solution(X, A):
    #Create a list to keep track of positions with leaves
    leaves=[]
    #Go through each leaf and its time
    for time in range(len(A)):
        #If this position has not been seen before
        if A[time] not in leaves:
            #Add the position to the list
            leaves.append(A[time])
        #If all positions from 1 to X have leaves
        if len(leaves)==X:
            return time
    #The frog can never cross
    return -1

