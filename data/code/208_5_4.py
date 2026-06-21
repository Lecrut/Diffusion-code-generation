def calculate_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    result = calculate_mean(numbers)
    print(f"Mean of {numbers}: {result}")