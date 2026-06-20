def filter_and_average(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return sum(positive_numbers) / len(positive_numbers) if positive_numbers else 0.0

if __name__ == '__main__':
    sample_values = [-5, 10, -3, 20, 0, 15, -1]
    average_result = filter_and_average(sample_values)
    print(average_result)