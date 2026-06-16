def reverse_generator(iterable):
    return (item for item in reversed(iterable))
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    reversed_data = reverse_generator(data)
    result = list(reversed_data)
    print(result)