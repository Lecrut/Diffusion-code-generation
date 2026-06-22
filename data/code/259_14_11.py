def get_extremes(nums):
    return (min(nums), max(nums)) if nums else None

if __name__ == '__main__':
    sample = [3, 5, 1, 2, 4]
    print(get_extremes(sample))
    empty = []
    print(get_extremes(empty))