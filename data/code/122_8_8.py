def calculate_average(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return sum(positive_numbers) / len(positive_numbers) if positive_numbers else None

if __name__ == '__main__':
    sample_values = [-1, 2, -3, 4, 5]
    average = calculate_average(sample_values)
    print(f"The average of positive numbers is: {average}")