def reverse_iterable(iterable):
    return list(reversed(list(iterable)))
if __name__ == '__main__':
    data = [10, 20, 30, 40]
    print(reverse_iterable(data))