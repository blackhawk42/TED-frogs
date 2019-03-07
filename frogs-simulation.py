import random
from fractions import Fraction

SIMULATIONS = 100000

FROG_MALE = 1
FROG_FEMALE = 2

def genPairWithOneMale():
    while True:
        pair = (random.randint(1, 2), random.randint(1, 2))
        if FROG_MALE in pair:
            break
    
    return pair

if __name__ == '__main__':
    print("************* Starting simulation *************")
    print("Starting with the hiker always going for the one silent frog:")

    hiker_status = {
        "alive": 0,
        "dead": 0,
    }

    for i in range(SIMULATIONS):
        print("Running simulation number {}".format(i+1), end="")
        frog = random.randint(1, 2)
        if frog == FROG_FEMALE:
            hiker_status["alive"] += 1
        else:
            hiker_status["dead"] += 1
        
        if i != SIMULATIONS-1:
            print('\r', end='')
        else:
            print("\n", end='')
    
    print("Stats:")
    total = hiker_status["dead"] + hiker_status["alive"]
    print("Total: {}".format(total))
    print("Times dead:  {} ({}, %{:.4f})".format(hiker_status["dead"],
                                            Fraction(hiker_status["dead"], total),
                                            (hiker_status["dead"]/total)*100))
    print("Times alive: {} ({}, %{:.4f})".format(hiker_status["alive"],
                                            Fraction(hiker_status["alive"], total),
                                            (hiker_status["alive"]/total)*100))
    
    print("\n\n", end='')
    
    total = 0
    hiker_status["alive"] = 0
    hiker_status["dead"] = 0
    
    print("Now the hiker will always go with the pair where one frog croaked")
    for i in range(SIMULATIONS):
        print("Running simulation number {}".format(i+1), end="")
        pair = genPairWithOneMale()
        if FROG_FEMALE in pair:
            hiker_status["alive"] += 1
        else:
            hiker_status["dead"] += 1
        
        if i != SIMULATIONS-1:
            print('\r', end='')
        else:
            print("\n", end='')
    

print("Stats:")
total = hiker_status["dead"] + hiker_status["alive"]
print("Total: {}".format(total))
print("Times dead:  {} ({}, %{:.4f})".format(hiker_status["dead"],
                                        Fraction(hiker_status["dead"], total),
                                        (hiker_status["dead"]/total)*100))
print("Times alive: {} ({}, %{:.4f})".format(hiker_status["alive"],
                                        Fraction(hiker_status["alive"], total),
                                        (hiker_status["alive"]/total)*100))

        