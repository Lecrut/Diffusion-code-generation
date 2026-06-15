import sys
def find_middle(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        return sorted_numbers[n // 2 - 1] or sorted_numbers[n // 2]
if __name__ == '__main__':
    sample_input = [10, 5, 20, 15, 30]
    try:
        number_list = []
        for item in sample_input:
            number_list.append(int(item))
        middle_value = find_middle(number_list)
        print(middle_value)
    except ValueError:
        print("Error: Invalid input. Please ensure all provided values are numeric.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")