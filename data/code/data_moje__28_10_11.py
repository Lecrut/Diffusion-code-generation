def sort_pair(a: int, b: int) -> tuple:
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_pair(3, 1))