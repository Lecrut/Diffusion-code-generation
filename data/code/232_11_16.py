START = 1
FACTOR = 2
ITERATIONS = 5

def generate_growing_sequence(start=START, factor=FACTOR, iterations=ITERATIONS):
    for _ in range(iterations):
        print(start)
        start *= factor

if __name__ == '__main__':
    generate_growing_sequence()