from itertools import permutations

def generate_permutations(numbers):
    return list(permutations(numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3]
    perms = generate_permutations(sample_values)
    print(perms)