def sort_by_criteria(data):
    return sorted(data, key=lambda x: (-x['primary'], x['secondary']))

if __name__ == '__main__':
    sample_data = [
        {'primary': 3, 'secondary': 1},
        {'primary': 2, 'secondary': 4},
        {'primary': 3, 'secondary': 2},
        {'primary': 1, 'secondary': 5},
        {'primary': 2, 'secondary': 3},
    ]
    sorted_data = sort_by_criteria(sample_data)
    for item in sorted_data:
        print(item)