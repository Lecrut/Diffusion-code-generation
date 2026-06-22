def find_largest_integer(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    [largest := n if n > largest else largest for n in numbers[1:]]
    return largest

if __name__ == '__main__':
    sample_numbers = [42, 17, 99, 3, 55, 88, 101, 12, 7, 250]
    result = find_largest_integer(sample_numbers)
    print(result)