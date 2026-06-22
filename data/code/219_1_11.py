def max_element(iterable):
    if not iterable:
        raise ValueError('Empty iterable')
    return max(iterable)
if __name__ == '__main__':
    print(max_element([3, 5, 1, 2, 4]))
    try:
        print(max_element([]))
    except ValueError as e:
        print(e)