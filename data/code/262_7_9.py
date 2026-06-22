def find_extremes(nested_list):
    if isinstance(nested_list, list):
        return min(find_extremes(sublist) for sublist in nested_list), max(find_extremes(sublist) for sublist in nested_list)
    else:
        return nested_list, nested_list

if __name__ == '__main__':
    sample = [[3, 5], [1, 2], [4, 6]]
    print(find_extremes(sample))