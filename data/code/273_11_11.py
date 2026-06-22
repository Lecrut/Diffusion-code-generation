def process_indices():
    indices = []
    squared_values = []

    for i in range(5):
        indices.append(i)
        squared_values.append(i ** 2)

    return indices, squared_values

if __name__ == '__main__':
    indices, squared_values = process_indices()
    print(indices)
    print(squared_values)