def average_of_positives(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return sum(positive_numbers) / len(positive_numbers) if positive_numbers else 0

if __name__ == '__main__':
    sample_values = [-1, 2, -3, 4, 5]
    print(average_of_positives(sample_values))