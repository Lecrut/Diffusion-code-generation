def sort_with_custom_key(data):
    return sorted(data, key=lambda x: x[0], reverse=True)
if __name__ == '__main__':
    sample_data = [(3, 1), (1, 0), (4, 2), (2, 3)]
    sorted_data = sort_with_custom_key(sample_data)
    print(sorted_data)