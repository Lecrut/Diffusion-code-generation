def sort_descending(x, y, z):
    values = (x, y, z)
    sorted_values = tuple(sorted(values, reverse=True))
    return sorted_values

if __name__ == '__main__':
    sample_values = (9, 7, 5)
    result = sort_descending(*sample_values)
    print(result)