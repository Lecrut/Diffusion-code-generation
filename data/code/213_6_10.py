from itertools import permutations

def generate_permutations(numbers):
    if len(numbers) != 3:
        raise ValueError("Input must contain exactly three numbers")
    return list(permutations(numbers))

if __name__ == '__main__':
    sample_numbers = (1, 2, 3)
    try:
        perms = generate_permutations(sample_numbers)
        print(perms)
    except ValueError as e:
        print(e)