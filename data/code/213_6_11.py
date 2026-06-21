from itertools import permutations

class NumberPermutator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def get_permutations(self):
        return list(permutations(self.numbers))

if __name__ == '__main__':
    sample_numbers = (1, 2, 3)
    permutator = NumberPermutator(sample_numbers)
    perms = permutator.get_permutations()
    for perm in perms:
        print(perm)