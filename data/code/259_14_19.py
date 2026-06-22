def get_extremes(lst):
    if not lst:
        return None
    try:
        return (min(lst), max(lst))
    except TypeError as e:
        print(f"Invalid input: {e}")
        return None

if __name__ == '__main__':
    print(get_extremes([3, 1, 4, 1, 5, 9]))
    print(get_extremes([-1, -5, -3]))
    print(get_extremes([]))