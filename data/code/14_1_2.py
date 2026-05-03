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
    print(f"Comparing {a} and {b}: {compare_volumes(a, b)}")
    a = 25.0
    b = 15.75
    print(f"Comparing {a} and {b}: {compare_volumes(a, b)}")
    a = 5.0
    b = 10.0
    print(f"Comparing {a} and {b}: {compare_volumes(a, b)}")