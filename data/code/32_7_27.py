class StringUtility:
    @staticmethod
    def calculate_length(input_string):
        return len(input_string)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    length_of_sample = StringUtility.calculate_length(sample_string)
    print(length_of_sample)