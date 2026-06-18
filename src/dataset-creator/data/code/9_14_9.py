import statistics
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [10, 25.5, 30, 45.75, 18]
    try:
        numeric_data = []
        for item in sample_numbers:
            if isinstance(item, (int, float)):
                numeric_data.append(float(item))
            else:
                raise ValueError("Invalid data type encountered.")
        if numeric_data:
            average = calculate_average(numeric_data)
            print(f"Input numbers processed: {numeric_data}")
            print(f"The calculated average is: {average:.2f}")
        else:
            print("No valid numerical data was provided for calculation.")
    except ValueError as e:
        print(f"Error during processing: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")