def sort_mixed_data(data):
    return sorted(data, key=lambda item: str(item).lower())

if __name__ == '__main__':
    data = [3, "apple", 1, "banana", 2]
    sorted_data = sort_mixed_data(data)
    print(sorted_data)