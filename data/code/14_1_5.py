def compare_volumes(vol1, vol2):
    if vol1 > vol2:
        return "Volume 1 is larger"
    elif vol1 < vol2:
        return "Volume 2 is larger"
    else:
        return "Volumes are equal"
if __name__ == '__main__':
    a = 10.5
    b = 15.2
    print(compare_volumes(a, b))
    x = 7.0
    y = 7.0
    print(compare_volumes(x, y))
    p = 3.14159
    q = 3.14
    print(compare_volumes(p, q))