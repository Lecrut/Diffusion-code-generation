def find_minimum(numbers):
    if not numbers:
        return None
    return min(numbers)

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 57, 90, 1]
    result = find_minimum(sample_list)
    print(result)