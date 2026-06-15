import statistics
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [10, 25.5, 30, 15.75, 40]
    try:
        numeric_data = []
        for item in sample_numbers:
            if isinstance(item, (int, float)):
                numeric_data.append(float(item))
            else:
                raise ValueError(f"Invalid input type encountered: {item}")
        if numeric_data:
            average = calculate_average(numeric_data)
            print(f"The entered numbers are: {numeric_data}")
            print(f"The calculated average is: {average:.2f}")
        else:
            print("No valid numerical data was processed.")
    except ValueError as e:
        print(f"An error occurred during processing: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")