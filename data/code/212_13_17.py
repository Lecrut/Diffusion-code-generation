def find_min_max(numbers):
    if not numbers:
        return None
    minimum = min(numbers)
    maximum = max(numbers)
    return (minimum, maximum)

if __name__ == '__main__':
    sample_list = [12, 34, 56, 78, 90, 10]
    result = find_min_max(sample_list)
    print(result)