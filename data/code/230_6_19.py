def reverse_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    if step == 0:
        raise ValueError("Step cannot be zero")
    for i in range(stop - 1, start - 1, -step):
        yield i

if __name__ == '__main__':
    for item in reverse_range(5):
        print(item)