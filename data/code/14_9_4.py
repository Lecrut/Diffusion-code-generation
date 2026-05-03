def compare_volumes(volume1: float, volume2: float) -> str:
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2"
    elif volume1 < volume2:
        return "Volume 1 is less than Volume 2"
    else:
        return "Volume 1 is equal to Volume 2"
if __name__ == '__main__':
    v1 = 150.75
    v2 = 150.75
    print(f"Comparing {v1} and {v2}: {compare_volumes(v1, v2)}")
    v3 = 200.0
    v4 = 100.5
    print(f"Comparing {v3} and {v4}: {compare_volumes(v3, v4)}")
    v5 = 50.0
    v6 = 75.2
    print(f"Comparing {v5} and {v6}: {compare_volumes(v5, v6)}")