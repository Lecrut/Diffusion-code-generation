def position_generator(data, index):
    for i, item in enumerate(data):
        if i == index:
            yield item
if __name__ == '__main__':
    large_list = list(range(1000000))
    target_index = 500000
    generator = position_generator(large_list, target_index)
    result = list(generator)
    print(result)