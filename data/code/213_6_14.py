from itertools import permutations

def generate_permutations(t):
    if not all(isinstance(i, (int, float)) and isinstance(j, (int, float)) and isinstance(k, (int, float)) for i in t):
        raise ValueError("All elements in the tuple must be numbers.")
    return list(permutations(t))

if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    result = generate_permutations(sample_tuple)
    print(result)