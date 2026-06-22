def safe_first(seq):
    if len(seq) == 0:
        raise IndexError("Sequence is empty")
    return seq[0]

if __name__ == '__main__':
    print(safe_first([1, 2, 3]))
    print(safe_first('hello'))
    try:
        safe_first([])
    except IndexError as e:
        print(str(e))