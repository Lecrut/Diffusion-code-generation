def count_unique_elements(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return sorted(counts.items())

if __name__ == '__main__':
    sample_numbers = [3, 1, 2, 2, 4, 3, 5]
    print(count_unique_elements(sample_numbers))