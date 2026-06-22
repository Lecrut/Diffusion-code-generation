def extract_first(sequence):
    if not sequence:
        raise IndexError("Sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    try:
        result1 = extract_first([1, 2, 3])
        print(result1)
    except IndexError as e:
        print(e)

    try:
        result2 = extract_first([])
        print(result2)
    except IndexError as e:
        print(e)

    try:
        result3 = extract_first("hello")
        print(result3)
    except IndexError as e:
        print(e)