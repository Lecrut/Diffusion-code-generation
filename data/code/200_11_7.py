def second_elements_generator(data):
    for index in range(0, len(data), 2):
        yield data[index]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gen = second_elements_generator(sample_data)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))