def sort_mixed_data(data):
    if not all(isinstance(item, (int, str)) for item in data):
        raise ValueError("All elements must be either integers or strings")
    return sorted(map(str, data))

if __name__ == '__main__':
    mixed_data = [3, "apple", 1, "banana", 2]
    sorted_mixed_data = sort_mixed_data(mixed_data)
    print(sorted_mixed_data)