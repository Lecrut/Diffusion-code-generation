from itertools import permutations

class PermutationGenerator:
    def __init__(self, data):
        self.data = data
        self.permutations = list(permutations(data))

    def get_permutations(self):
        return self.permutations

if __name__ == '__main__':
    sample_data = (1, 2, 3)
    generator = PermutationGenerator(sample_data)
    perms = generator.get_permutations()
    for perm in perms:
        print(perm)