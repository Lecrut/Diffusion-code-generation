def sum_adjacent_pairs(numbers):
    sums = []
    for i in range(len(numbers) - 1):
        pair_sum = numbers[i] + numbers[i+1]
        sums.append(pair_sum)
    return sums
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = sum_adjacent_pairs(data)
    print(result)