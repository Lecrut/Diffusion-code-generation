def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = []
    sample3 = [10, 20, 30]

    try:
        print(f"Average of {sample1}: {calculate_average(sample1)}")
    except ValueError as e:
        print(e)

    try:
        print(f"Average of {sample2}: {calculate_average(sample2)}")
    except ValueError as e:
        print(e)

    try:
        print(f"Average of {sample3}: {calculate_average(sample3)}")
    except ValueError as e:
        print(e)