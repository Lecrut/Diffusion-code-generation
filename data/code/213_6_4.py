from itertools import permutations

def generate_permutations(numbers):
    return list(permutations(numbers))

if __name__ == '__main__':
    sample_numbers = (1, 2, 3)
    print(generate_permutations(sample_numbers))