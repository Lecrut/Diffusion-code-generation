def calculate_mean(numbers):
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_data)
    print(result)