def alternate_elements(data):
    for index in range(0, len(data), 2):
        yield data[index]

if __name__ == '__main__':
    sample_data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    gen = alternate_elements(sample_data)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))