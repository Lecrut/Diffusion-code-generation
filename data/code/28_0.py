def sort_pair(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    result = sort_pair(3, 1)
    print(result)