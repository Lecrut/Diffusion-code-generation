import statistics
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [10, 25.5, 30, 45, 12]
    try:
        numerical_data = []
        for item in sample_numbers:
            numerical_data.append(float(item))
        average = calculate_average(numerical_data)
        if average is not None:
            print(f"The entered numbers are: {numerical_data}")
            print(f"The calculated average is: {average:.2f}")
        else:
            print("No valid numerical data was provided.")
    except ValueError:
        print("Error: One or more inputs could not be converted to a valid number. Please ensure all inputs are numerical.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")