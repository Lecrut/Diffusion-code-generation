def compute_average(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(compute_average(sample_numbers))