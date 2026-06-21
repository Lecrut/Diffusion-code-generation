def filter_unique(numbers):
    seen = set()
    unique_numbers = []
    for number in numbers:
        if number not in seen:
            unique_numbers.append(number)
            seen.add(number)
    return unique_numbers
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    filtered_numbers = filter_unique(sample_numbers)
    print(filtered_numbers)