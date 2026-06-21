from itertools import permutations

def generate_permutations(numbers):
    if not all(isinstance(num, int) and 0 <= num < 1000 for num in numbers):
        raise ValueError("Input list must contain only integers between 0 and 999.")
    
    perms = permutations(numbers)
    return [list(p) for p in perms]

if __name__ == '__main__':
    sample_numbers = [3, 5, 7]
    all_perms = generate_permutations(sample_numbers)
    print(all_perms)