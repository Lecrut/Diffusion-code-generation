def find_middle_integer(numbers):
    if not numbers:
        return None
    n = len(numbers)
    middle_index = n // 2
    if n % 2 == 1:
        return numbers[middle_index]
    else:
        return numbers[middle_index - 1] or numbers[middle_index]
if __name__ == '__main__':
    sample_input = [10, 20, 30, 40, 50]
    try:
        input_list = []
        for item in sample_input:
            if not isinstance(item, int):
                raise ValueError("Input contains non-integer values.")
            input_list.append(item)
        if not input_list:
            print("Input list is empty.")
        else:
            middle = find_middle_integer(input_list)
            print(middle)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")