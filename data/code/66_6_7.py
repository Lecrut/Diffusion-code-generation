def kilometers_to_meters_generator(kilometers):
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    sample_kilometers = [1, 2.5, 10, 0.05]
    for value in kilometers_to_meters_generator(sample_kilometers):
        print(value)