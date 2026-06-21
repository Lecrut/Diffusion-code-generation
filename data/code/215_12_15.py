def find_max(iterable):
    try:
        return max(iterable)
    except ValueError:
        return None

if __name__ == '__main__':
    print(find_max([3, 5, 1, 2]))
    print(find_max([]))
    print(find_max([-1, -3, -2]))