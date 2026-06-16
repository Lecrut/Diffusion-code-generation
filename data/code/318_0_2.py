def calculate_adjacent_sum(numbers):
    sums = []
    for i in range(len(numbers) - 1):
        sums.append(numbers[i] + numbers[i+1])
    return sums
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = calculate_adjacent_sum(data)
    print(result)