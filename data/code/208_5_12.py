def calculate_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    numbers = [15, 25, 35, 45, 55]
    mean = calculate_mean(numbers)
    print(f"Mean of {numbers}: {mean}")