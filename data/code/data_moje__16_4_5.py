def get_first(sequence):
    if not sequence:
        raise IndexError("Sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    print(get_first([1, 2, 3]))
    print(get_first(('a', 'b')))
    try:
        get_first([])
    except IndexError as e:
        print(str(e))