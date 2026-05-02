class LengthCalculator:
    @staticmethod
    def calculate_length(data):
        return len(data)
if __name__ == '__main__':
    sample_string = "hello world"
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    print(f"Length of '{sample_string}': {LengthCalculator.calculate_length(sample_string)}")
    print(f"Length of {sample_list}: {LengthCalculator.calculate_length(sample_list)}")
    print(f"Length of {sample_tuple}: {LengthCalculator.calculate_length(sample_tuple)}")