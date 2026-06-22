def calculate_sum(sequence: list[int]) -> int:
    total = 0
    for number in sequence:
        total += number
    return total

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    result = calculate_sum(sample_sequence)
    print(result)