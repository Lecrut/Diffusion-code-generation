from itertools import permutations

def generate_permutations(values):
    if not all(isinstance(x, int) and 0 <= x < 1000 for x in values):
        raise ValueError("Values must be integers between 0 and 999.")
    
    return sorted(set(permutations(values)))

if __name__ == '__main__':
    sample_values = [1, 2, 3]
    perms = generate_permutations(sample_values)
    print(perms)