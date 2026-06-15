import sys
def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    input_data = "10 5 -2 8 1"
    numbers = []
    is_valid = True
    for item in input_data.split():
        try:
            number = float(item)
            numbers.append(number)
        except ValueError:
            is_valid = False
            break
    if not is_valid:
        print("Error: Input contains non-numeric data.")
    elif not numbers:
        print("Error: No valid numeric data found.")
    else:
        try:
            minimum_value = find_minimum(numbers)
            print(minimum_value)
        except ValueError as e:
            print(f"Error processing data: {e}")