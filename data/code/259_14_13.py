def get_extremes(nums):
    return (min(nums), max(nums)) if nums else None

if __name__ == '__main__':
    print(get_extremes([3, 1, 4, 1, 5, 9]))
    print(get_extremes([]))