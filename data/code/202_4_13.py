def max_element(*args):
    if not args:
        raise ValueError("No elements provided")
    return max(args)

if __name__ == '__main__':
    try:
        print(max_element(10, 5, 20, 8, 15))
    except ValueError as e:
        print(e)