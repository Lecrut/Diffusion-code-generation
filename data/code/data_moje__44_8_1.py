def compute_mean(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    total = 0
    count = 0
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("All elements must be integers")
        total += number
        count += 1
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)