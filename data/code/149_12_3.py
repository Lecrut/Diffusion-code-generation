import sys
def reverse_list(data):
    return data[::-1]
if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5]
    try:
        numbers = []
        for item in sample_input:
            if not isinstance(item, int):
                raise ValueError("Input must be an integer.")
            numbers.append(item)
        reversed_numbers = reverse_list(numbers)
        print(reversed_numbers)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")