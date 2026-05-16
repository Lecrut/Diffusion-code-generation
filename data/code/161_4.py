def item_generator(data):
    for item in data:
        yield item
if __name__ == '__main__':
    sample_list = list(range(1, 100))
    generator = item_generator(sample_list)
    first_ten = []
    for _ in range(10):
        first_ten.append(next(generator))
    print(first_ten)