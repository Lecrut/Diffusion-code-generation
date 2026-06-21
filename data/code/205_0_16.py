def sort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = [15, 7, 24, 3, 6]
    sorted_data = sort_ascending(sample_values)
    print(*sorted_data)