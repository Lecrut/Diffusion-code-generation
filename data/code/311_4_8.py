def reverse_iterator(iterable):
    return reversed(iterable)
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    generator = reverse_iterator(data)
    result = list(generator)
    print(result)