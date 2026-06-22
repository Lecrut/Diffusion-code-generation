def get_extremes(numbers):
    return (min(numbers), max(numbers)) if numbers else None

if __name__ == '__main__':
    sample = [3, 5, 1, 2, 4]
    print(get_extremes(sample))
    empty_list = []
    print(get_extremes(empty_list))