import itertools

def generate_permutations(numbers):
    if not isinstance(numbers, tuple) or len(numbers) != 3:
        raise ValueError("Input must be a tuple of three distinct numbers")
    
    permutations = list(itertools.permutations(numbers))
    return permutations

if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    result = generate_permutations(sample_tuple)
    print(result)