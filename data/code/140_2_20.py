def is_sorted_ascending(lst):
    return all(x <= y for x, y in zip(lst, lst[1:]))

if __name__ == '__main__':
    sample_values = [3, 5, 8, 9, 10]
    print(is_sorted_ascending(sample_values))