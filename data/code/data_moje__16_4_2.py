def first_element(seq):
    if not seq:
        raise IndexError("Sequence is empty")
    return seq[0]

if __name__ == '__main__':
    print(first_element([1, 2, 3]))
    print(first_element("hello"))
    try:
        first_element([])
    except IndexError as e:
        print(e)