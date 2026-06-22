def get_extremes(lst):
    try:
        return (min(lst), max(lst))
    except ValueError:
        return None

if __name__ == '__main__':
    print(get_extremes([3, 1, 4, 1, 5, 9]))
    print(get_extremes([]))
    print(get_extremes([-1, -5, -3]))