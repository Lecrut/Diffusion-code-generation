def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

if __name__ == '__main__':
    sample_list = [34, 12, 45, 2, 99, 15]
    result = find_min(sample_list)
    print(result)