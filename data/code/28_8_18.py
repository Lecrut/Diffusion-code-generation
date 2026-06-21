def sort_pair(a, b):
    if a <= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    result = sort_pair(5, 2)
    print(result)
    result = sort_pair(1, 10)
    print(result)
    result = sort_pair(3.5, 2.1)
    print(result)