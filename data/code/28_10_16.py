def sort_pair(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_pair(5, 3))