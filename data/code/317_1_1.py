def cycle_range(start, end):
    for i in range(start, end + 1):
        yield i
if __name__ == '__main__':
    print(list(cycle_range(1, 5)))
    print(list(cycle_range(10, 12)))