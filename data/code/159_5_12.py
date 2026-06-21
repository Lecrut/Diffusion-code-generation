class OddNumberFilter:
    def __init__(self, data):
        self.data = data

    def filter_odds(self):
        return tuple(num for num in self.data if num % 2 != 0)

if __name__ == '__main__':
    sample_sequence = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    filter_instance = OddNumberFilter(sample_sequence)
    odd_numbers = filter_instance.filter_odds()
    print(odd_numbers)