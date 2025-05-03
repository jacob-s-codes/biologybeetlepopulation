import random

pop = ["Bb"] * 12 + ["bb"] * 6
pop_size = 18
Bb_count = 0
BB_count = 0
bb_count = 0
B_count = 0
b_count = 0
num_generations = 100
def mate(p1, p2): #Will give a1 and a2 either B or b
    a1 = random.choice(p1)
    a2 = random.choice(p2)
    return ''.join(sorted([a1, a2])) # Bb == bB

def create_offspring():
    offspring = []
    for i in range(pop_size):
        p1 = random.choice(pop)
        p2 = random.choice(pop)
        child = mate(p1, p2)
        offspring.append(child)
    return offspring

def run():
    for i in range(num_generations):
        run = create_offspring()
        BB_count = bb_count = Bb_count = B_count = b_count = 0 # Reset counts
        for child in run:
            if child == "Bb":
                Bb_count+=1
                B_count += 1
                b_count +=1
            elif child == "BB":
                B_count += 2
                BB_count += 1
            else:
                bb_count+=1
                b_count +=2

        B_count /= 36
        b_count /= 36

        print("Generation: " + str(i))
        print("Bb count: " + str(Bb_count))
        print("bb count: " + str(bb_count))
        print("BB count: " + str(BB_count))
        print("\n")
        print("\n")
        print("B^2: " + str(B_count**2) + ", b^2: " + str(b_count**2), ", 2Bb: " + str(2*B_count*b_count))

run()



# print(pop)