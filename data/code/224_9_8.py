def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(f"Mean of {data}: {calculate_mean(data)}")