def cumulative_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(cumulative_sum(sample_values))