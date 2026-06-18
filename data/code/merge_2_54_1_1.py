def calculate_center(iterable):
    try:
        iterator = iter(iterable)
        length = 0
        while True:
            item = next(iterator, None)
            if item is not None:
                length += 1
            else:
                break
        center_index = (length - 1) // 2
        return center_index
    except TypeError:
        raise ValueError("Input must be an iterable sequence")
if __name__ == '__main__':
    data_tuple = (10, 20, 30, 40)
    center_pos = calculate_center(data_tuple)
    print(f"Center index: {center_pos}")