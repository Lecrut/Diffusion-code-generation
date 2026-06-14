def find_middle_value(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        return (middle1 + middle2) / 2
if __name__ == '__main__':
    sample_input_str = "10, 5, 8, 2, 15"
    try:
        input_list = [int(x.strip()) for x in sample_input_str.split(',')]
        middle = find_middle_value(input_list)
        print(f"The input list is: {input_list}")
        if middle is not None:
            print(f"The middle value is: {middle}")
        else:
            print("The list is empty.")
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are valid numbers separated by commas.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")