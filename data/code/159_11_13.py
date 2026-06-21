class OddNumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def odd_integers(self):
        for value in self.numbers:
            if value % 2 != 0:
                yield value

if __name__ == '__main__':
    sample_values = [11, 13, 15, 17, 19, 20, 22]
    filter_instance = OddNumberFilter(sample_values)
    for odd_value in filter_instance.odd_integers():
        print(odd_value)