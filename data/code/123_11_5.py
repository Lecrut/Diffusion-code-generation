def cumulative_sum(numbers):
    result = []
    current_sum = 0
    for number in numbers:
        current_sum += number
        result.append(current_sum)
    return result

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(cumulative_sum(sample_numbers))