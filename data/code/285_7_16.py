def compare_adjacent_numbers(numbers):
    return ['ascending' if numbers[i] < numbers[i+1] else 'descending' if numbers[i] > numbers[i+1] else 'equal' for i in range(len(numbers)-1)]

if __name__ == '__main__':
    sample_values = [3.5, 2.8, 4.1, 4.1, 1.9]
    print(compare_adjacent_numbers(sample_values))