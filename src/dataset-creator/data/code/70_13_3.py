def compare_distances(d1: float, d2: float) -> bool:
    if abs(d1 - d2) < 0.0001:
        return True
    elif d1 > d2:
        return False
    else:
        return True
if __name__ == '__main__':
    result = compare_distances(5.0, 5.00009)
    print(result)