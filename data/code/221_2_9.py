def sort_descending(x, y, z):
    return tuple(sorted([x, y, z], reverse=True))

if __name__ == '__main__':
    result = sort_descending(3, 1, 2)
    print(result)