def conditional_sum(a: int | float = 10, b: int | float = 20, c: int | float = 30) -> int | None:
    if (x := a).__class__ in (int, float) and\
       (y := b).__class__ in (int, float) and\
       (z := c).__class__ in (int, float):
        return x + y + z
    return None
if __name__ == '__main__':
    result = conditional_sum(10.5, 20, '30')
    print(result if isinstance(result, int) else result)