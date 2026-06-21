def first_element(seq):
    if len(seq) == 0:
        raise IndexError("sequence is empty")
    return seq[0]

if __name__ == '__main__':
    print(first_element([1, 2, 3]))
    print(first_element(('a', 'b')))
    print(first_element([42]))
    try:
        print(first_element([]))
    except IndexError as e:
        print(e)