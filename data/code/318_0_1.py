def calculate_adjacent_sums(numbers):
    sums = []
    for i in range(len(numbers) - 1):
        sum_val = numbers[i] + numbers[i+1]
        sums.append(sum_val)
    return sums
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = calculate_adjacent_sums(data)
    print(result)