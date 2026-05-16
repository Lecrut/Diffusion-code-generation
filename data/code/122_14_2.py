import sys
def calculate_average(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    input_data = sample_input.split()
    numbers = []
    error_occurred = False
    for item in input_data:
        try:
            numbers.append(float(item))
        except ValueError:
            error_occurred = True
            break
    if error_occurred:
        print("Error: Invalid input detected. Please ensure all inputs are numeric.")
    else:
        if numbers:
            average = calculate_average(numbers)
            print(average)
        else:
            print("No valid numbers were provided.")