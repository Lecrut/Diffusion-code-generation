def compare_lengths(d1, c1, d2, c2):
    total_cm1 = d1 * 10 + c1
    total_cm2 = d2 * 10 + c2
    if total_cm1 > total_cm2:
        return f"{d1}dm {c1}cm"
    else:
        return f"{d2}dm {c2}cm"

if __name__ == '__main__':
    print(compare_lengths(5, 3, 4, 8))