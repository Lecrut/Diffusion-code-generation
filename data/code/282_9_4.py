def calculate_sum(sequence: list[int]) -> int:
    if not all(isinstance(num, int) for num in sequence):
        raise ValueError("All elements in the sequence must be integers")
    total = 0
    for number in sequence:
        total += number
    return total

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = calculate_sum(data)
    print(result)