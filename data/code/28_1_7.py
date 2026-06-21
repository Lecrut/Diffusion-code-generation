def sort_descending(a, b):
    return sorted([a, b], reverse=True)

if __name__ == '__main__':
    x = 5
    y = 10
    result = sort_descending(x, y)
    print(result)