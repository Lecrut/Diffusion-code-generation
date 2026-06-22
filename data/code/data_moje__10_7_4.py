def sequence_generator():
    values = [42, 17, 99, 3]
    for item in values:
        yield item

if __name__ == '__main__':
    gen = sequence_generator()
    first_item = next(gen)
    print(first_item)