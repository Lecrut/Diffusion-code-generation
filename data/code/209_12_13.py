def average_generator(numbers):
    count = 0
    total = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("All elements must be numbers")
        count += 1
        total += number
    return total / count if count > 0 else None

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(average_generator(sample_values))