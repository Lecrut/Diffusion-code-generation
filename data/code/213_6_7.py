from itertools import permutations

def generate_permutations():
    numbers = (1, 2, 3)
    return list(permutations(numbers))

if __name__ == '__main__':
    print(generate_permutations())