def get_extremes(lst):
    return (min(lst), max(lst)) if lst else None

if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 15]
    print(get_extremes(sample_values))
    empty_list = []
    print(get_extremes(empty_list))