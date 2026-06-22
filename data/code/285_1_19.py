def compare_adjacent_pairs(numbers):
    results = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            results.append('ascending')
        elif numbers[i] > numbers[i + 1]:
            results.append('descending')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_values = [5, 3, 8, 8, 2]
    print(compare_adjacent_pairs(sample_values))