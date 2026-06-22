def calculate_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [1.5, 2.5, 3.0, 4.0, 5.0]
    result = calculate_mean(sample_data)
    print(result)
    try:
        calculate_mean([])
    except ValueError as e:
        print(e)