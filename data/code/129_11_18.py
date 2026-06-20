def sort_tuples(data):
    return sorted(data, key=lambda x: (-x[0], x[1]))

if __name__ == '__main__':
    sample_data = [(3, 'apple'), (1, 'banana'), (2, 'cherry'), (3, 'date')]
    print(sort_tuples(sample_data))