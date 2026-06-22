def get_ordered_pair(a, b):
    if a < b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    result = get_ordered_pair(5, 3)
    print(result)
    result = get_ordered_pair(10, 10)
    print(result)
    result = get_ordered_pair(1, 100)
    print(result)