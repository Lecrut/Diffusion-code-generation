def sort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = [12, 45, 78, 34, 6, 90]
    result = sort_ascending(sample_values)
    print(*result)