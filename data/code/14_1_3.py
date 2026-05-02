def compare_volumes(vol1: float, vol2: float) -> str:
    if vol1 > vol2:
        return "Volume 1 is larger"
    elif vol1 < vol2:
        return "Volume 2 is larger"
    else:
        return "Volumes are equal"
if __name__ == '__main__':
    a = 10.5
    b = 10.5
    print(compare_volumes(a, b))
    x = 25.7
    y = 15.3
    print(compare_volumes(x, y))
    p = 500.0
    q = 1200.5
    print(compare_volumes(p, q))