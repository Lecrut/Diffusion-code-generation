def calculate_mean(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [10, 25, 32, 48, 15]
    try:
        if not isinstance(sample_numbers, list):
            raise TypeError("Input must be a list of numbers.")
        numeric_numbers = []
        for item in sample_numbers:
            if isinstance(item, (int, float)):
                numeric_numbers.append(item)
            else:
                print(f"Skipping invalid input: {item}")
        if numeric_numbers:
            mean_value = calculate_mean(numeric_numbers)
            print(f"The numbers entered are: {numeric_numbers}")
            print(f"The arithmetic mean is: {mean_value}")
        else:
            print("No valid numbers were provided to calculate the mean.")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")