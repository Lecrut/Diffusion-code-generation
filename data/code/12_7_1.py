def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1], sequence[length // 2])

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([1]))
    print(get_middle_element([1, 2]))
    print(get_middle_element("abc"))
    print(get_middle_element("abcd"))
    print(get_middle_element("a"))
    print(get_middle_element("ab"))
    try:
        get_middle_element([])
    except ValueError as e:
        print(str(e))