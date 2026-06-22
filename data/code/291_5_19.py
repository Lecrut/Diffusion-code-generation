def compare_measures(d1, c1, d2, c2):
    total_c1 = d1 * 10 + c1
    total_c2 = d2 * 10 + c2
    if total_c1 > total_c2:
        return f"{d1} decimeters and {c1} centimeters"
    else:
        return f"{d2} decimeters and {c2} centimeters"

if __name__ == '__main__':
    print(compare_measures(3, 50, 4, 20))