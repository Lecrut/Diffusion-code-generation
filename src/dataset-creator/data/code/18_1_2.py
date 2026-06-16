def reverse_iterable(iterable):
    return list(reversed(list(iterable)))
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    reversed_data = reverse_iterable(data)
    print(f"Original: {data}")
    print(f"Reversed: {reversed_data}")