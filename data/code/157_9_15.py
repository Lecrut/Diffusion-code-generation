class NumberProcessor:
    ERROR_MESSAGE = "Input list cannot be empty"

    @staticmethod
    def find_smallest_iterative(data):
        if not data:
            raise ValueError(NumberProcessor.ERROR_MESSAGE)
        smallest = data[0]
        for element in data[1:]:
            if element < smallest:
                smallest = element
        return smallest

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 78]
    try:
        result = NumberProcessor.find_smallest_iterative(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")