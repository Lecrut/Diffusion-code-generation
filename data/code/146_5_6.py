import itertools

def generate_permutations(numbers):
    return list(itertools.permutations(numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3]
    permutations = generate_permutations(sample_numbers)
    print(permutations)