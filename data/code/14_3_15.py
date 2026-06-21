def third_element(iterable):
    return next((item for index, item in enumerate(iterable) if index == 2), None)

if __name__ == '__main__':
    print(third_element([1, 2, 3, 4, 5]))
    print(third_element((1, 2, 3, 4, 5)))
    print(third_element('hello'))
    print(third_element([1, 2]))
    print(third_element(x for x in range(10)))