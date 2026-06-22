def max_element(iterable):
    if not iterable:
        raise ValueError("Empty iterable")
    return max(iterable)

if __name__ == '__main__':
    try:
        print(max_element([3, 1, 4, 1, 5, 9]))
    except ValueError as e:
        print(e)