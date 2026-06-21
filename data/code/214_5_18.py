def smallest_positive(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return min(positive_numbers) if positive_numbers else None

if __name__ == '__main__':
    sample_values = [-5, -3, 1, 2, 4]
    print(smallest_positive(sample_values))