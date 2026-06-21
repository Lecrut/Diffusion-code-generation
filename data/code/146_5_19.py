from itertools import permutations

def generate_permutations(numbers):
    if not all(isinstance(num, int) and 0 <= num < 1000 for num in numbers):
        raise ValueError("All elements must be integers between 0 and 999")
    return list(permutations(numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3]
    perms = generate_permutations(sample_values)
    print(perms)