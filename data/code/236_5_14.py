import numpy as np

def repeat_square_pattern(base_shape, repetitions):
    square = np.array([["#"] * len(base_shape)] * len(base_shape))
    tiled_pattern = np.tile(square, (repetitions, repetitions))
    return tiled_pattern.tolist()

if __name__ == '__main__':
    base_shape = ["##", "# ", "##"]
    repetitions = 3
    pattern = repeat_square_pattern(base_shape, repetitions)
    for row in pattern:
        print(" ".join(row))