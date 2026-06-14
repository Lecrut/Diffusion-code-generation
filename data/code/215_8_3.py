def find_maximum(*args):
    if not args:
        return None
    maximum = args[0]
    for num in args[1:]:
        if num > maximum:
            maximum = num
    return maximum
if __name__ == '__main__':
    print(find_maximum(10, 5, 20, 8))
    print(find_maximum(-3, -1, -5))
    print(find_maximum(42))
    print(find_maximum())