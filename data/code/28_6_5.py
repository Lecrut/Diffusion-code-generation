def sort_pair(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    x = 10
    y = 5
    result = sort_pair(x, y)
    print(result)