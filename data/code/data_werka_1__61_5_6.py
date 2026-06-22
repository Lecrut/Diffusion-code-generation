def element_generator(iterable_list, position):
    for index, item in enumerate(iterable_list):
        if index == position:
            yield item

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    position_to_fetch = 2
    generator = element_generator(sample_list, position_to_fetch)
    for value in generator:
        print(value)