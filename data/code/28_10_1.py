def sort_two_integers(a: int, b: int) -> tuple[int, int]:
    if a <= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    x = 10
    y = 5
    result = sort_two_integers(x, y)
    print(result)