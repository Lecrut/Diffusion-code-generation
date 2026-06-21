from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    print(generate_permutations(sample_list))