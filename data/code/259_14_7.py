def get_extremes(lst):
    return (min(lst), max(lst)) if lst else None

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 7]
    print(get_extremes(sample_values))
    print(get_extremes([]))