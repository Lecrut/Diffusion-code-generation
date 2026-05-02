def compare_volumes(vol1, vol2):
    if vol1 > vol2:
        return "Volume 1 is larger"
    elif vol1 < vol2:
        return "Volume 2 is larger"
    else:
        return "Volumes are equal"
if __name__ == '__main__':
    a = 15.5
    b = 22.1
    print(compare_volumes(a, b))
    x = 100.0
    y = 100.0
    print(compare_volumes(x, y))
    p = 5.0
    q = 1.2
    print(compare_volumes(p, q))