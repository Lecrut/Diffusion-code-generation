def element_generator(iterable, position):
    for index, value in enumerate(iterable):
        if index == position:
            yield value

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_position = 2
    generator = element_generator(sample_list, target_position)
    for item in generator:
        print(item)