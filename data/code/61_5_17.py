def element_at_position(iterable, position):
    for index, item in enumerate(iterable):
        if index == position:
            yield item

if __name__ == '__main__':
    test_list = [100, 200, 300, 400, 500]
    target_position = 3
    generator = element_at_position(test_list, target_position)
    for value in generator:
        print(value)