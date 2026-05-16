def find_middle(numbers):
    if not numbers:
        return None
    n = len(numbers)
    middle_index = n // 2
    if n % 2 == 1:
        return numbers[middle_index]
    else:
        return numbers[middle_index - 1] or numbers[middle_index]
if __name__ == '__main__':
    sample_input_str = "10, 20, 30, 40, 50"
    try:
        input_list = [int(x.strip()) for x in sample_input_str.split(',')]
        if not input_list:
            print("Input list is empty.")
        else:
            print(f"Input sequence: {input_list}")
            middle_value = find_middle(input_list)
            if middle_value is not None:
                print(f"The middle integer is: {middle_value}")
            else:
                print("Could not determine the middle integer.")
    except ValueError:
        print("Error: Input contains non-integer values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")