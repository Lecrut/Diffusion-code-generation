min_value = lambda lst: min(lst) if lst else None
if __name__ == '__main__':
    print(min_value([4, 2, 9, 7]))
    print(min_value([1]))
    print(min_value([]))