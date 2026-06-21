def filter_duplicates(numbers):
    unique = []
    i = 0
    while i < len(numbers):
        if numbers[i] not in unique:
            unique.append(numbers[i])
        i += 1
    return unique

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(filter_duplicates(sample_values))