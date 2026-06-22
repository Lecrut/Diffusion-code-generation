def get_extremes(numbers):
    return (min(numbers), max(numbers)) if numbers else None

if __name__ == '__main__':
    print(get_extremes([3, 1, 4, 1, 5, 9]))
    print(get_extremes([]))
    print(get_extremes([-2, -6, -3]))