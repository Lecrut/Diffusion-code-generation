def get_extremes(source):
    mapping = {True: (0, -1), False: (0, 0)}
    try:
        items = list(source)
        if not items:
            raise ValueError("empty input")
        indices = mapping[len(items) > 1]
        return (items[indices[0]], items[indices[1]])
    except TypeError:
        raise ValueError("not iterable")

if __name__ == '__main__':
    print(get_extremes([4, 8, 15, 16, 23, 42]))
    try:
        print(get_extremes([]))
    except ValueError as e:
        print(e)
    print(get_extremes("hello"))