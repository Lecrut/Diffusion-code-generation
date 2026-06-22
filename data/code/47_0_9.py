def calculate_mean(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7, 4.2]
    result = calculate_mean(sample_values)
    print(result)