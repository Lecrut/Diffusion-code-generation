def find_min_max(numbers):
    if not numbers:
        return None, None
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum

if __name__ == '__main__':
    sample_data2 = [8, 14, 3, 7, 19, 5]
    min2, max2 = find_min_max(sample_data2)
    print(f"Data set 2: {sample_data2}")
    print(f"Minimum: {min2}, Maximum: {max2}")