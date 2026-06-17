def reverse_iterator(iterable):
    for item in reversed(iterable):
        yield item
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    reversed_data = list(reverse_iterator(data))
    print(reversed_data)
    data2 = "abcdef"
    reversed_data2 = list(reverse_iterator(data2))
    print(reversed_data2)