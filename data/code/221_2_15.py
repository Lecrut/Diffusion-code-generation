def sort_descending(x, y, z):
    temp = (x, y, z)
    sorted_values = tuple(sorted(temp, reverse=True))
    return sorted_values

if __name__ == '__main__':
    sample_values = (9, 4, 6)
    result = sort_descending(*sample_values)
    print(result)