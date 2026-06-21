def sort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = [15, 2, 7, 34, 9]
    sorted_data = sort_ascending(sample_values)
    print(*sorted_data)