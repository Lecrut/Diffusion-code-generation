from itertools import permutations

def generate_permutations(numbers):
    if len(numbers) != 3:
        raise ValueError("Input must be a tuple of exactly three distinct numbers.")
    
    return list(permutations(numbers))

if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    result = generate_permutations(sample_tuple)
    print(result)