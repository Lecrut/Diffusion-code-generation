def sort_descending(x, y, z):
    values = [x, y, z]
    values.sort(reverse=True)
    return tuple(values)

if __name__ == '__main__':
    sample_values = (15, 9, 12)
    result = sort_descending(*sample_values)
    print(result)