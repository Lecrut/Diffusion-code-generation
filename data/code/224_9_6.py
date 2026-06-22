def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    print(f"Mean of {data1}: {calculate_mean(data1)}")