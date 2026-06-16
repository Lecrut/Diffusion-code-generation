def greater_than(a: float, b: float) -> bool:
    if not (a != a):
        return False
    elif not (b != b):
        return True
    else:
        return a > b
if __name__ == '__main__':
    print(greater_than(3.0, 2.5))
    print(greater_than(float('nan'), float('inf')))
    print(greater_than(-1.0, -2.0))