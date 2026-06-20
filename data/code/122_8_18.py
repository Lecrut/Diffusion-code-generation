def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def calculate_average(filtered_numbers):
    if not filtered_numbers:
        return 0.0
    return sum(filtered_numbers) / len(filtered_numbers)

def main():
    input_string = "10,-20,30,40,-50"
    try:
        number_strings = input_string.split(',')
        numbers = [float(num.strip()) for num in number_strings]
        positive_numbers = filter_positive_numbers(numbers)
        average = calculate_average(positive_numbers)
        print(f"The average of positive numbers is: {average}")
    except ValueError:
        print("Error: Invalid input. Please ensure all parts are valid numbers.")

if __name__ == '__main__':
    main()