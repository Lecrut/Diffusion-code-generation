import statistics
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [10, 25.5, 30, 15.75, 40]
    try:
        numerical_data = []
        for item in sample_numbers:
            if isinstance(item, (int, float)):
                numerical_data.append(float(item))
            else:
                raise ValueError("Invalid data type encountered.")
        if numerical_data:
            average = calculate_average(numerical_data)
            print(f"Input numbers: {numerical_data}")
            print(f"The calculated average is: {average:.2f}")
        else:
            print("No valid numerical data was provided.")
    except ValueError as e:
        print(f"Error processing input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")