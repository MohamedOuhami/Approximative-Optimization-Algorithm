import math,random,time

# Setting my variables

n = 8  # The number of items
max_Iterations = 10000  # The maximum number of iterations allowed
V = [10,15,40,2,5,3,1,20]  # The value of each items
W = [30,15,20,1,5,2,1,3] # The weight of each item
X = [0,0,0,0,0,0,0,0] # The choice list
max_weight = 13 # The weight constraint

# The objective function == Calculate the value of the sac
def value():
    r = 0
    for i in range(n):
        r+= V[i]*X[i]
    return r

# The weight function == Calculate the weight of the sac
def weight():
    r = 0
    for i in range(n):
        r += W[i]*X[i]

    return r

# The constraints == Return 1 if the sac is valid, and 0 if the sac exceeds the nax weight

def constraint():
    d = weight()
    
    if(d<=max_weight):
        return 1
    else : return 0

# The printing method
def showX():
    print("The solution is ",end=' ')
    print("[",end='')
    for i in range(n):
        print(X[i],end=' ')
    print("]")

def showV():
    print("The solution for V is ",end=' ')
    print("[")
    for i in range(n):
        print(V[i],end=' ')
    print("]")

def showW():
    print("The weights are ",end=' ')
    print("[")
    for i in range(n):
        print(W[i],end=' ')
    print("]")

# Creating a new choice list
def RandSol():
    for i in range(n):
        X[i] = random.randint(0, 1)


# Going through the iterations and fetch the max value with the optimal weight
def RandAlgo():
    # index
    k = 0
    # Starting the f_max at 0
    f_max = 0
    
    while True :
        # Randomize the choice list
        RandSol()
        # If the value of the sac is superior to the max_value and Its weight is inferior to the max_weight
        if(value()>f_max and constraint() == 1):
            # Setting the new max value
            f_max = value()
            print(f_max)
        k += 1

        # Breaking The loop
        if(k > max_Iterations):
            break

    return f_max

print(RandAlgo())

