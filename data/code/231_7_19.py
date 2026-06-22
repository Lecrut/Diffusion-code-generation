import numpy as np

PATTERN = [True, False]
NUM_ITERATIONS = 25

def generate_pattern():
    if hasattr(np, 'ndarray'):
        return np.tile(PATTERN, (1, NUM_ITERATIONS))
    else:
        return PATTERN * (NUM_ITERATIONS // len(PATTERN)) + PATTERN[:NUM_ITERATIONS % len(PATTERN)]

if __name__ == '__main__':
    pattern = generate_pattern()
    print("Generated pattern:")
    for i in range(0, len(pattern), 5):
        print(pattern[i:i+5])