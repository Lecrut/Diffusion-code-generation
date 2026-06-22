def reverse_range(start, stop):
    if start >= stop:
        raise ValueError("Start must be less than stop for a valid range")
    for i in range(stop - 1, start - 1, -1):
        yield i

if __name__ == '__main__':
    try:
        for item in reverse_range(5, 0):
            print(item)
    except ValueError as e:
        print(e)