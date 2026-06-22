def sort_descending(a, b, c):
    values = (a, b, c)
    sorted_values = tuple(sorted(values, reverse=True))
    return sorted_values

if __name__ == '__main__':
    result = sort_descending(3, 1, 2)
    print(result)