import itertools

class NumberSequence:
    def __init__(self):
        self.sequence = list(itertools.count(1))

    def get_first_n_numbers(self, n=20):
        return self.sequence[:n]

if __name__ == '__main__':
    sequence_instance = NumberSequence()
    first_20_numbers = sequence_instance.get_first_n_numbers()
    for number in first_20_numbers:
        print(number)