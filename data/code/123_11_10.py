def calculate_cumulative_sum(numbers):
    cumulative_sum = 0
    result = []
    for number in numbers:
        cumulative_sum += number
        result.append(cumulative_sum)
    return result

if __name__ == '__main__':
    sample_numbers = [3, 6, -2, 4, 5]
    cumsum_result = calculate_cumulative_sum(sample_numbers)
    print(cumsum_result)