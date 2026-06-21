class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        if not self.numbers:
            raise ValueError("Input iterable cannot be empty")
        return max(self.numbers)

if __name__ == '__main__':
    sample_dict = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
    finder = MaxFinder(sample_dict.values())
    print(f"Maximum of {sample_dict}: {finder.find_max()}")