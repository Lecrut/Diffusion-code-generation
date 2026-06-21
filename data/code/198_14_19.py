class StringMinimizer:
    @staticmethod
    def find_smallest_string(strings):
        if not strings:
            raise ValueError("The list is empty.")
        return min(strings)

if __name__ == '__main__':
    sample_strings = ["banana", "apple", "cherry"]
    try:
        smallest_string = StringMinimizer.find_smallest_string(sample_strings)
        print(smallest_string)
    except ValueError as e:
        print(e)