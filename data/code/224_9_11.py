def calculate_mean(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    try:
        print(f"Mean of {data1}: {calculate_mean(data1)}")
    except ValueError as e:
        print(e)