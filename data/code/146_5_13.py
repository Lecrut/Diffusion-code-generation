from itertools import permutations

class PermutationGenerator:
    def __init__(self, numbers):
        self.numbers = numbers

    def generate_permutations(self):
        return list(permutations(self.numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3]
    generator = PermutationGenerator(sample_numbers)
    perms = generator.generate_permutations()
    for perm in perms:
        print(perm)