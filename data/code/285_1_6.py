def compare_adjacent_elements(numbers):
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
    sample_values = [3, 5, 2, 8, 6, 6]
    print(compare_adjacent_elements(sample_values))