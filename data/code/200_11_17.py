def second_elements_generator(data):
    for index in range(1, len(data), 2):
        yield data[index]

if __name__ == '__main__':
    sample_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    gen = second_elements_generator(sample_data)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))