import itertools

class PermutationGenerator:
    def __init__(self, numbers):
        self.numbers = numbers

    def generate_permutations(self):
        return list(itertools.permutations(self.numbers))

if __name__ == '__main__':
    generator = PermutationGenerator([1, 2, 3])
    permutations = generator.generate_permutations()
    for perm in permutations:
        print(perm)