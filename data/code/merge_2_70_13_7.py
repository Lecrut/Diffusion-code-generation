def compare_distances(d1: float, d2: float) -> str:
    if d1 < d2:
        return "d1 is closer"
    elif d2 < d1:
        return "d2 is closer"
    else:
        return "distances are equal"
if __name__ == '__main__':
    result = compare_distances(5.0, 3.0)
    print(result)