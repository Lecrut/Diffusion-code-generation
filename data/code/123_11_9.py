def calculate_cumulative_sum(numbers):
    cumulative_sums = []
    current_sum = 0
    for number in numbers:
        current_sum += number
        cumulative_sums.append(current_sum)
    return cumulative_sums

if __name__ == '__main__':
    sample_list = [1, 5, 10, 2, 8]
    result = calculate_cumulative_sum(sample_list)
    print(result)