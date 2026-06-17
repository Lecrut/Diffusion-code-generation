def compare_adjacent(numbers):
    differences = []
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        differences.append(diff)
    return differences
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    result = compare_adjacent(sample_list)
    print(result)