def yield_first_value():
    vector = [10, 20, 30]
    yield vector[0]

if __name__ == '__main__':
    generator = yield_first_value()
    value = next(generator)
    print(value)