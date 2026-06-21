def get_middle_item(sequence):
    try:
        length = len(sequence)
        if length == 0:
            return None
        if length % 2 == 1:
            return sequence[length // 2]
        else:
            return (sequence[length // 2 - 1], sequence[length // 2])
    except TypeError:
        return None
    except IndexError:
        return None

if __name__ == '__main__':
    print(get_middle_item([1, 2, 3]))
    print(get_middle_item([1, 2, 3, 4]))
    print(get_middle_item([]))
    print(get_middle_item([5]))
    print(get_middle_item([1, 2]))
    print(get_middle_item("hello"))
    print(get_middle_item("world"))
    print(get_middle_item("hi"))
    print(get_middle_item(None))
    print(get_middle_item(123))