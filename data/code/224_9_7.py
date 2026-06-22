def calculate_mean(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    try:
        mean = calculate_mean(data)
        print(f"Mean of {data}: {mean}")
    except ValueError as e:
        print(e)