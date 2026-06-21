def find_smallest_iterative(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest

class SmallestFinder:
    MIN_VALUE_ERROR = "Input list cannot be empty"

    @staticmethod
    def find_smallest(data):
        if not data:
            raise ValueError(SmallestFinder.MIN_VALUE_ERROR)
        smallest = data[0]
        for element in data[1:]:
            if element < smallest:
                smallest = element
        return smallest

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    try:
        result = find_smallest_iterative(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    finder = SmallestFinder()
    sample_list_2 = [100, 50, 200, 10]
    try:
        result = finder.find_smallest(sample_list_2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")