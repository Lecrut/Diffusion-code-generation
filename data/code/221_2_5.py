def sort_desc(a, b, c):
    return tuple(sorted((a, b, c), reverse=True))

if __name__ == '__main__':
    result = sort_desc(3, 1, 2)
    print(result)