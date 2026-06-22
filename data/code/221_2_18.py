def sort_descending(x, y, z):
    return tuple(sorted([x, y, z], reverse=True))

if __name__ == '__main__':
    sample_values = (9, 3, 6)
    result = sort_descending(*sample_values)
    print(result)