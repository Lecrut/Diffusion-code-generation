def every_second_element():
    for index, value in enumerate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        if index % 2 == 1:
            yield value

if __name__ == '__main__':
    for element in every_second_element():
        print(element)