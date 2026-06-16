def reverse_iterable(iterable):
    return list(reversed(list(iterable)))
if __name__ == '__main__':
    original = [1, 2, 3, 4, 5]
    result = reverse_iterable(original)
    print(f"Original: {original}")
    print(f"Reversed: {result}")