def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(calculate_mean(sample_values))
    empty_list = []
    try:
        print(calculate_mean(empty_list))
    except ValueError as e:
        print(e)