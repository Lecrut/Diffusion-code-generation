def sort_pair(a, b):
    if a <= b:
        return a, b
    return b, a

if __name__ == '__main__':
    result = sort_pair(5, 2)
    print(result)