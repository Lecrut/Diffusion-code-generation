import sys
def find_max(data):
    try:
        if not data:
            raise ValueError("Input list is empty")
        return max(data)
    except TypeError as e:
        print(f"Error: {e}. Input must be iterable.")
        sys.exit(1)
if __name__ == '__main__':
    sample_list = [3, 5, -20, 4.7]
    try:
        result = find_max(sample_list)
        print(f"Largest element: {result}")
    except ValueError as ve:
        print(ve)