class LengthCalculator:
    @staticmethod
    def calculate_length(sequence):
        return len(sequence)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_list = [1, 2, 3, 4, 5]
    
    string_length = LengthCalculator.calculate_length(sample_string)
    list_length = LengthCalculator.calculate_length(sample_list)
    
    print(f"Length of the string: {string_length}")
    print(f"Length of the list: {list_length}")