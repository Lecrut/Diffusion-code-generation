def adjacent_boolean_generator(data):
    for i in range(len(data) - 1):
        yield data[i] != data[i+1]
if __name__ == '__main__':
    sample_list = [True, False, True, True, False]
    generator = adjacent_boolean_generator(sample_list)
    results = list(generator)
    print(results)