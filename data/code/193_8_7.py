def sum_generator(items):
    total = 0
    for item in items:
        total += item
        yield total

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    gen = sum_generator(sample_data)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))