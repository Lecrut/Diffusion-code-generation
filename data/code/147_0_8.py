def sort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    SAMPLE_LIST = [5, 2, 8, 1, 9, 3]
    sorted_data = sort_ascending(SAMPLE_LIST)
    print(*sorted_data)