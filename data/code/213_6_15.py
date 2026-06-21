from itertools import permutations

class NumberPermutator:
    NUMBERS = (1, 2, 3)

    @staticmethod
    def generate_permutations():
        return list(permutations(NumberPermutator.NUMBERS))

if __name__ == '__main__':
    permutator = NumberPermutator()
    result = permutator.generate_permutations()
    for perm in result:
        print(perm)