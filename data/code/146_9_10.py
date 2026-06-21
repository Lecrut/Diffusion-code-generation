def find_max_subarray_sum(numbers):
    current_sum = max_sum = numbers[0]
    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

if __name__ == '__main__':
    sample_values = [-2, 3, -4, 5, -6, 7, -8]
    print(find_max_subarray_sum(sample_values))