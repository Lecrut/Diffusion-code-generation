def find_middle_integer(numbers):
    if not numbers:
        return None
    n = len(numbers)
    if n % 2 == 1:
        middle_index = n // 2
        return numbers[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (numbers[middle_left_index] + numbers[middle_right_index]) // 2
if __name__ == '__main__':
    sample_input = [1, 5, 2, 8, 3]
    try:
        integer_list = [int(x) for x in sample_input]
        if not integer_list:
            print("Input list is empty.")
        else:
            n = len(integer_list)
            if n % 2 == 1:
                middle_index = n // 2
                print(integer_list[middle_index])
            else:
                middle_right_index = n // 2
                middle_left_index = middle_right_index - 1
                middle_value = (integer_list[middle_left_index] + integer_list[middle_right_index]) // 2
                print(middle_value)
    except ValueError:
        print("Error: Input contained non-integer values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")