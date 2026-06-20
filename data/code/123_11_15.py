def calculate_cumulative_sum(numbers):
    if not numbers:
        return 0
    cumsum = [numbers[0]]
    for number in numbers[1:]:
        cumsum.append(cumsum[-1] + number)
    return cumsum

if __name__ == '__main__':
    sample_array = [1, 5, 10, 2, 8]
    result = calculate_cumulative_sum(sample_array)
    print(result)