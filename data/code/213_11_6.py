def count_unique_elements(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return sorted(frequency.items())

if __name__ == '__main__':
    sample_numbers = [3, 1, 2, 3, 4, 2, 5, 1]
    print(count_unique_elements(sample_numbers))