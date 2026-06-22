def reverse_range(start, end):
    if start > end:
        return
    for i in range(end - 1, start - 1, -1):
        yield i

if __name__ == '__main__':
    for item in reverse_range(5, 10):
        print(item)