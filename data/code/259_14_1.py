def get_extremes(lst):
    return (min(lst), max(lst)) if lst else None

if __name__ == '__main__':
    print(get_extremes([3, 1, 4, 1, 5, 9, 2]))
    print(get_extremes([]))