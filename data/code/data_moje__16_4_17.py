def first_element(sequence):
    if not sequence:
        raise IndexError("sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    print(first_element([1, 2, 3]))
    print(first_element("hello"))
    try:
        first_element([])
    except IndexError as e:
        print(repr(e))