def filter_duplicates(numbers):
    unique_numbers = []
    seen = set()
    i = 0
    while i < len(numbers):
        if numbers[i] not in seen:
            unique_numbers.append(numbers[i])
            seen.add(numbers[i])
        i += 1
    return unique_numbers

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
    print(filter_duplicates(sample_values))