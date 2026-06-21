def sort_reverse(a, b):
    return sorted((a, b), reverse=True)

if __name__ == '__main__':
    x = 10
    y = 42
    result = sort_reverse(x, y)
    print(result)