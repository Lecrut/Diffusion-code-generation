def check_first_and_last(sequence):
    if not sequence:
        return None, None
    first = sequence[0]
    last = sequence[-1]
    return first, last
if __name__ == '__main__':
    print(check_first_and_last([1, 2, 3, 4, 5]))
    print(check_first_and_last("hello"))
    print(check_first_and_last([]))
    print(check_first_and_last([10]))
    print(check_first_and_last((1, 2, 3)))