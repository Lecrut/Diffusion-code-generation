import itertools

def generate_permutations(values):
    return list(itertools.permutations(values))

if __name__ == '__main__':
    sample_values = [1, 2, 3]
    permutations = generate_permutations(sample_values)
    print(permutations)