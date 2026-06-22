START = 0
END = -1

def reverse_range_generator(start=START, end=END):
    if start > end:
        return
    for i in range(end, start - 1, -1):
        yield i

if __name__ == '__main__':
    for item in reverse_range_generator(10, 5):
        print(item)