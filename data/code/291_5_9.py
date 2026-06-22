def compare_measures(d1, c1, d2, c2):
    total_c1 = d1 * 10 + c1
    total_c2 = d2 * 10 + c2
    if total_c1 > total_c2:
        return f"{d1}dm {c1}cm"
    else:
        return f"{d2}dm {c2}cm"

if __name__ == '__main__':
    result = compare_measures(6, 75, 5, 90)
    print(result)