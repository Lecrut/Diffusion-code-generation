def find_max(iterable):
    return max(iterable) if iterable else None
if __name__ == '__main__':
    print(find_max([3, 5, 1, 2, 4]))
    print(find_max([]))