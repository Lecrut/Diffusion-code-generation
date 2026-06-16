def reverse_iterable(iterable):
    return list(reversed(list(iterable)))
if __name__ == '__main__':
    data = [1, 2, 3]
    result = reverse_iterable(data)
    print(result)