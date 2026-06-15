class MinFinder:
    def __init__(self):
        self.numbers = []
    def add_numbers(self, numbers):
        self.numbers.extend(numbers)
    def get_minimum(self):
        if not self.numbers:
            return None
        minimum = self.numbers[0]
        for number in self.numbers[1:]:
            if number < minimum:
                minimum = number
        return minimum
if __name__ == '__main__':
    mf = MinFinder()
    sample_data1 = [10, 5, 20, 3, 15]
    mf.add_numbers(sample_data1)
    print(f"Minimum of {sample_data1}: {mf.get_minimum()}")
    mf2 = MinFinder()
    sample_data2 = [-5, 100, 0, -10]
    mf2.add_numbers(sample_data2)
    print(f"Minimum of {sample_data2}: {mf2.get_minimum()}")
    mf3 = MinFinder()
    sample_data3 = [42]
    mf3.add_numbers(sample_data3)
    print(f"Minimum of {sample_data3}: {mf3.get_minimum()}")
    mf4 = MinFinder()
    sample_data4 = []
    mf4.add_numbers(sample_data4)
    print(f"Minimum of {sample_data4}: {mf4.get_minimum()}")