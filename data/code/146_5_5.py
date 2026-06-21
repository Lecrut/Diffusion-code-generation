import itertools

def generate_permutations(lst):
    return list(itertools.permutations(lst))

if __name__ == '__main__':
    sample_values = [1, 2, 3]
    print(generate_permutations(sample_values))