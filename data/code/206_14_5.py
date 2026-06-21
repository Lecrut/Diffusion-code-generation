min_value = lambda lst: min(lst) if lst else None
if __name__ == '__main__':
    print(min_value([3, 1, 4, 1, 5]))
    print(min_value([7]))
    print(min_value([]))