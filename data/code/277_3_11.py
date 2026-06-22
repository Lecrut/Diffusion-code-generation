class EvenNumberCounter:
    def __init__(self):
        self.count = 0

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    def count_evens(self, iterable):
        iterator = iter(iterable)
        while True:
            try:
                item = next(iterator)
                if self.is_even(item):
                    self.count += 1
            except StopIteration:
                break

if __name__ == '__main__':
    counter = EvenNumberCounter()
    sample_list = [1, 2, 3, 4, 5]
    counter.count_evens(sample_list)
    print(f"Number of even numbers in {sample_list}: {counter.count}")