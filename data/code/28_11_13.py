def sort_descending(a: int | float, b: int | float) -> tuple:
    if a < b:
        return b, a
    return a, b

if __name__ == '__main__':
    print(sort_descending(3, 7))