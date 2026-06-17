def calculate_adjacent_sum(numbers):
    sums = []
    for i in range(len(numbers) - 1):
        current_sum = numbers[i] + numbers[i+1]
        sums.append(current_sum)
    return sums
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = calculate_adjacent_sum(sample_list)
    print(result)