def find_max(iterable):
    return max(iterable) if iterable else None

if __name__ == '__main__':
    print(find_max([3, 5, 1, 2]))
    print(find_max([]))
    print(find_max([-1, -3, -2]))
    print(find_max([4.5, 6.7, 5.3]))