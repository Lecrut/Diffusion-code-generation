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
    sample_list_1 = [15, 3, 8, 22, 1]
    mf.add_numbers(sample_list_1)
    print(f"Minimum of {sample_list_1}: {mf.get_minimum()}")
    sample_list_2 = [-5, 10, -2, 7]
    mf.add_numbers(sample_list_2)
    print(f"Minimum of {sample_list_2}: {mf.get_minimum()}")
    empty_list = []
    mf.add_numbers(empty_list)
    print(f"Minimum of empty list: {mf.get_minimum()}")