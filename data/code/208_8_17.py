def compute_average(numbers):
    numeric_values = [num for num in numbers if isinstance(num, int)]
    return sum(numeric_values) / len(numeric_values) if numeric_values else 0.0

if __name__ == '__main__':
    sample_data = [10, "a", 25, None, 30, "hello", 4]
    average_value = compute_average(sample_data)
    print(average_value)