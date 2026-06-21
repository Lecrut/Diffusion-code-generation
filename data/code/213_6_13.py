from itertools import permutations

def generate_permutations():
    numbers = (1, 2, 3)
    perms = list(permutations(numbers))
    return perms

if __name__ == '__main__':
    perms = generate_permutations()
    for perm in perms:
        print(perm)