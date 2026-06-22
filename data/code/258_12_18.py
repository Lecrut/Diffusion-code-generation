import numpy as np

def compute_average_pairs(pairs):
    if not isinstance(pairs, list) or not all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs):
        raise ValueError("Input must be a list of tuples, each containing exactly two numbers.")
    
    if len(pairs) == 0:
        return 0
    
    total_sum = np.sum([np.sum(pair) for pair in pairs])
    count = len(pairs)
    
    return total_sum / count

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6)]
    print(compute_average_pairs(sample_data))