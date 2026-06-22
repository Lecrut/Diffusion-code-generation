def get_extremes(lst):
    return (min(lst), max(lst)) if lst else None

if __name__ == '__main__':
    print(get_extremes([7, 3, 9, 2]))
    print(get_extremes([-1, -5, -3]))
    print(get_extremes([]))