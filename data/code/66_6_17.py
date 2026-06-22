def meter_generator(kilometers):
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    sample_inputs = [1, 2.5, 10, 0.001]
    for value in meter_generator(sample_inputs):
        print(value)