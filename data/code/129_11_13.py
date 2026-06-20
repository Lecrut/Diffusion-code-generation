def sort_data(data):
    return sorted(data, key=lambda x: (-x[0], x[1]))

if __name__ == '__main__':
    sample_data = [
        (3, 'Banana'),
        (2, 'Apple'),
        (3, 'Cherry'),
        (2, 'Date'),
        (3, 'Avocado'),
        (1, 'Carrot')
    ]
    sorted_data = sort_data(sample_data)
    for item in sorted_data:
        print(item)