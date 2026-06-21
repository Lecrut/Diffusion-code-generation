def max_element(*args):
    if not args:
        raise ValueError("No elements provided")
    return max(args)

if __name__ == '__main__':
    print(max_element(3, 5, 1, 2, 4))