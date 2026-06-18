import sys
def count_elements(collection):
    try:
        if not hasattr(collection, "__iter__"):
            raise TypeError("Input must be iterable")
        counter = 0
        for _ in collection:
            counter += 1
        return counter
    except Exception as e:
        print(f"Error processing input: {e}")
        sys.exit(1)
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b']
    try:
        result_count = count_elements(sample_data)
        print(result_count)
    except TypeError as te:
        print(f"Invalid input type: {te}")