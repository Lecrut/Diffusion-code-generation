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
    sample_list = [1, 2, 3, 4, 5]
    sample_string = "hello world"
    sample_tuple = (10, 20, 30)
    sample_integer = 12345
    print(f"Length of sample_list: {LengthCalculator.calculate_length(sample_list)}")
    print(f"Length of sample_string: {LengthCalculator.calculate_length(sample_string)}")
    print(f"Length of sample_tuple: {LengthCalculator.calculate_length(sample_tuple)}")
    print(f"Length of sample_integer: {LengthCalculator.calculate_length(sample_integer)}")