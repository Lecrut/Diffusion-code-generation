def find_middle_value(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        return sorted_numbers[n // 2 - 1], sorted_numbers[n // 2]
if __name__ == '__main__':
    sample_input = [10, 5, 20, 15, 30]
    numeric_list = []
    for item in sample_input:
        try:
            number = float(item)
            numeric_list.append(number)
        except ValueError:
            print(f"Error: '{item}' is not a valid number and will be skipped.")
    if numeric_list:
        middle_value = find_middle_value(numeric_list)
        if middle_value is None:
            print("The list is empty.")
        elif isinstance(middle_value, tuple):
            print(f"The middle values are: {middle_value[0]} and {middle_value[1]}")
        else:
            print(f"The middle value is: {middle_value}")
    else:
        print("No valid numbers were entered.")