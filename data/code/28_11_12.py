def sort_two_descending(a: float, b: float) -> tuple[float, float]:
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_two_descending(5, 10))