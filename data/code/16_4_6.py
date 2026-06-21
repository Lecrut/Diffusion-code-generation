def safe_first(seq):
    if not seq:
        raise IndexError("Sequence is empty")
    return seq[0]

if __name__ == '__main__':
    print(safe_first([1, 2, 3]))
    print(safe_first('hello'))
    print(safe_first((4, 5, 6)))
    try:
        safe_first([])
    except IndexError as e:
        print(e)
    try:
        safe_first(())
    except IndexError as e:
        print(e)
    try:
        safe_first('')
    except IndexError as e:
        print(e)