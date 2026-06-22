def get_first_item(data):
    iterator = iter(data)
    try:
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    numbers = [5, 10, 15]
    print(get_first_item(numbers))
    print(get_first_item([]))
    print(get_first_item([99]))