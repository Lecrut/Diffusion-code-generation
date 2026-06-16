def calculate_running_total(numbers):
    running_total = 0
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All inputs must be numbers.")
        running_total += num
    return running_total
if __name__ == '__main__':
    sample_input = [10, 5.5, -3, 20]
    try:
        result = calculate_running_total(sample_input)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")