import sys
def find_middle(numbers):
    if not numbers:
        return None
    n = len(numbers)
    middle_index = n // 2
    return numbers[middle_index]
if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    try:
        input_list = [int(x) for x in sample_input.split()]
        middle_value = find_middle(input_list)
        print(middle_value)
    except ValueError:
        print("Error: Input contains non-integer values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")