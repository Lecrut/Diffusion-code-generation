import numpy as np

def create_tiled_pattern(base_shape, num_repetitions):
    if not isinstance(base_shape, np.ndarray) or base_shape.ndim != 2:
        raise ValueError("base_shape must be a 2D NumPy array")
    
    if not isinstance(num_repetitions, int) or num_repetitions < 1:
        raise ValueError("num_repetitions must be a positive integer")
    
    tiled_pattern = np.tile(base_shape, (num_repetitions, num_repetitions))
    return tiled_pattern

if __name__ == '__main__':
    base_square = np.array([[0, 1],
                             [1, 0]])
    try:
        pattern = create_tiled_pattern(base_square, 3)
        print("Tiled Pattern:")
        print(pattern)
    except ValueError as e:
        print(e)