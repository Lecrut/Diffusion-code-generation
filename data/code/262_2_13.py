def find_min_max(numbers):
    if not numbers:
        return None, None
    min_val = max_val = numbers[0]
    for number in numbers:
        if number < min_val:
            min_val = number
        elif number > max_val:
            max_val = number
    return min_val, max_val

if __name__ == '__main__':
    sample_data2 = [8, 12, 4, 16, 7]
    min2, max2 = find_min_max(sample_data2)
    print(f"Data set 2: {sample_data2}")
    print(f"Minimum: {min2}, Maximum: {max2}")