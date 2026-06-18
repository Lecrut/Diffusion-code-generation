import statistics
def calculate_average(numbers):
    if not numbers:
        return None
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        return None
if __name__ == '__main__':
    sample_values = [10, 25.5, 30, 45, 18]
    numerical_data = []
    for item in sample_values:
        try:
            numerical_data.append(float(item))
        except ValueError:
            print(f"Error: '{item}' is not a valid number and will be skipped.")
            continue
    if numerical_data:
        average = calculate_average(numerical_data)
        print(f"Input values processed: {numerical_data}")
        print(f"The calculated average is: {average}")
    else:
        print("No valid numerical data was entered to calculate the average.")