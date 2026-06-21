def sort_two_descending(a: int | float, b: int | float) -> tuple[int | float, int | float]:
    if a < b:
        return (b, a)
    return (a, b)

if __name__ == '__main__':
    result = sort_two_descending(10, 20)
    print(result)