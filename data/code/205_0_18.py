def sort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = [45, 21, 36, 89, 12, 7]
    sorted_data = sort_ascending(sample_values)
    print(*sorted_data)