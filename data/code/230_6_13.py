def reverse_range(start, stop):
    if start >= stop:
        return
    yield from range(stop - 1, start - 1, -1)

if __name__ == '__main__':
    for item in reverse_range(0, 5):
        print(item)