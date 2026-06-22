def compute_mean(numbers: list[int]) -> float:
    if not numbers:
        raise ValueError("List must not be empty")
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = compute_mean(sample_numbers)
    print(result)