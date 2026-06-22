def sort_descending(a: float, b: float) -> list:
    if a >= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    x = 10.5
    y = 3.2
    result = sort_descending(x, y)
    print(result)