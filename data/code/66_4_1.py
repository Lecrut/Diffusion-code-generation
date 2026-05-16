def adjacent_boolean_generator(data):
    for i in range(len(data) - 1):
        yield data[i] != data[i+1]
if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 1, 4]
    generator = adjacent_boolean_generator(sample_list)
    results = list(generator)
    print(results)