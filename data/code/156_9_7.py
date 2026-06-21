def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"The average is: {calculate_average(sample_list)}")