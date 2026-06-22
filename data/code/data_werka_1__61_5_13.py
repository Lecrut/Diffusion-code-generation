def element_generator(iterable, position):
    for index, item in enumerate(iterable):
        if index == position:
            yield item

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_position = 2
    generator = element_generator(sample_list, target_position)
    for value in generator:
        print(value)