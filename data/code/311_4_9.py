def reverse_generator(iterable):
    for item in reversed(iterable):
        yield item
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print(list(reverse_generator(data)))