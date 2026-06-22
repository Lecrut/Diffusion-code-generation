def get_first_last(iterable):
    try:
        items = list(iterable)
        if not items:
            raise ValueError("iterable is empty")
        return (items[0], items[-1])
    except TypeError:
        raise ValueError("input is not iterable")

if __name__ == '__main__':
    print(get_first_last([10, 20, 30]))
    try:
        print(get_first_last([]))
    except ValueError as e:
        print(e)
    print(get_first_last("abc"))