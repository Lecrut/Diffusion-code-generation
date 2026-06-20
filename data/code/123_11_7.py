def calculate_cumulative_sum(numbers):
    cumulative_sum = 0
    for number in numbers:
        cumulative_sum += number
    return cumulative_sum

if __name__ == '__main__':
    sample_list = [1, 5, 10, 2, 8]
    result = calculate_cumulative_sum(sample_list)
    print(result)