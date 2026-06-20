def cumulative_sum(numbers):
    total = 0
    result = []
    for number in numbers:
        total += number
        result.append(total)
    return result

if __name__ == '__main__':
    sample_values = [3, 7, 2, 5, 8]
    computed_result = cumulative_sum(sample_values)
    print(computed_result)