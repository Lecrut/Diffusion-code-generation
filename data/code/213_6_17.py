from itertools import permutations

def generate_permutations(numbers):
    return list(permutations(numbers))

if __name__ == '__main__':
    sample_numbers = (7, 8, 9)
    result = generate_permutations(sample_numbers)
    for perm in result:
        print(perm)