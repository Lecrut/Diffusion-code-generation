def calculate_average(numbers):
    try:
        positive_numbers = [num for num in numbers if num > 0]
        if not positive_numbers:
            return "No positive numbers found."
        return sum(positive_numbers) / len(positive_numbers)
    except TypeError:
        return "Error: Invalid input. Please ensure all elements are integers."

if __name__ == '__main__':
    sample_values = [10, -5, 20, 30, 40]
    average = calculate_average(sample_values)
    print(average)