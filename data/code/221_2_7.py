def sort_descending(a, b, c):
    return tuple(sorted((a, b, c), reverse=True))

if __name__ == '__main__':
    result = sort_descending(3, 1, 2)
    print(result)