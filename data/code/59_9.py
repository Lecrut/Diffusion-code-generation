def find_middle_integer(numbers):
    if not numbers:
        return None
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) // 2
if __name__ == '__main__':
    sample_input = [1, 5, 2, 8, 3]
    try:
        integer_list = []
        for item in sample_input:
            if isinstance(item, int):
                integer_list.append(item)
            else:
                raise ValueError("Input contains non-integer values.")
        if not integer_list:
            print("No valid integers found.")
        else:
            n = len(integer_list)
            if n % 2 == 1:
                middle_index = n // 2
                middle_value = integer_list[middle_index]
                print(middle_value)
            else:
                middle_index_right = n // 2
                middle_index_left = middle_index_right - 1
                middle_value = (integer_list[middle_index_left] + integer_list[middle_index_right]) // 2
                print(middle_value)
    except ValueError as e:
        print(f"Error processing input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")