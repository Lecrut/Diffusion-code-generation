def sort_pair(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    result = sort_pair(5, 2)
    print(result)
    result2 = sort_pair(-1, 3)
    print(result2)
    result3 = sort_pair(10, 10)
    print(result3)