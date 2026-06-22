def compare_measures(d1, c1, d2, c2):
    total_cm1 = d1 * 10 + c1
    total_cm2 = d2 * 10 + c2
    if total_cm1 > total_cm2:
        return f"{d1}dm {c1}cm"
    elif total_cm2 > total_cm1:
        return f"{d2}dm {c2}cm"
    else:
        return "Equal"

if __name__ == '__main__':
    print(compare_measures(3, 50, 4, 7))