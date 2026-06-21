def sort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = [45, 23, 67, 12, 89, 34]
    sorted_data = sort_ascending(sample_values)
    print(*sorted_data)