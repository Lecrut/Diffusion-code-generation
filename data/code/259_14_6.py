def get_extremes(lst):
    if not lst:
        return None
    return (min(lst), max(lst))

if __name__ == '__main__':
    print(get_extremes([3, 1, 4, 1, 5, 9]))
    print(get_extremes([]))