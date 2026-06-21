def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(sample_numbers)
    print(avg)