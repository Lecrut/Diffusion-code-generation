def adjacent_pairs(data):
    for i in range(len(data) - 1):
        yield (data[i], data[i+1])
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result_generator = adjacent_pairs(sample_data)
    output = list(result_generator)
    print(output)