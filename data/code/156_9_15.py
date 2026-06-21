def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return 0
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        return 0

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"Average of {sample_list}: {calculate_average(sample_list)}")