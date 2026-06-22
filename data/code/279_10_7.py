def cycle_range():
    number_map = {i: i for i in range(1, 11)}
    for number in number_map.values():
        print(number)

if __name__ == '__main__':
    cycle_range()