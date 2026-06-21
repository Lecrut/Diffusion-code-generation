from itertools import permutations
SAMPLE_TUPLE = (1, 2, 3)

def generate_permutations(input_tuple):
    return list(permutations(input_tuple))
if __name__ == '__main__':
    result = generate_permutations(SAMPLE_TUPLE)
    print(result)