class LengthCalculator:
    @staticmethod
    def calculate_length(data):
        if isinstance(data, (list, tuple)):
            return len(data)
        elif isinstance(data, str):
            return len(data)
        else:
            return 0
if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = "hello world"
    sample3 = 12345
    sample4 = {"a": 1, "b": 2}
    print(f"Length of {sample1}: {LengthCalculator.calculate_length(sample1)}")
    print(f"Length of '{sample2}': {LengthCalculator.calculate_length(sample2)}")
    print(f"Length of {sample3}: {LengthCalculator.calculate_length(sample3)}")
    print(f"Length of {sample4}: {LengthCalculator.calculate_length(sample4)}")