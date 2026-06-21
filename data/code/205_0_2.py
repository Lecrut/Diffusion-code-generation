def sort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = [10, 4, 2, 3, 8, 5]
    sorted_data = sort_ascending(sample_values)
    print(*sorted_data)