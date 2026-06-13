import sys
def find_middle(numbers):
    if not numbers:
        return None
    n = len(numbers)
    middle_index = n // 2
    return numbers[middle_index]
if __name__ == '__main__':
    input_str = "10,20,30,40,50"
    try:
        numbers = [int(x.strip()) for x in input_str.split(',')]
        middle_value = find_middle(numbers)
        print(middle_value)
    except ValueError:
        print("Error: Input contained non-integer values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")