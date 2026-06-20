def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def calculate_average(filtered_numbers):
    if not filtered_numbers:
        return 0.0
    return sum(filtered_numbers) / len(filtered_numbers)

if __name__ == '__main__':
    sample_input = [10, -20, 30, -40, 50]
    positive_numbers = filter_positive_numbers(sample_input)
    average = calculate_average(positive_numbers)
    print(f"Positive numbers: {positive_numbers}")
    print(f"Average of positive numbers: {average}")