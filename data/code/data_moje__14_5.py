def get_third_item(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == '__main__':
    print(get_third_item([1, 2, 3, 4, 5]))
    print(get_third_item("hello"))
    try:
        get_third_item([1, 2])
    except IndexError as e:
        print(e)