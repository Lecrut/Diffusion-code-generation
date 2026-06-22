def validate_length(d, c):
    if not isinstance(d, int) or not isinstance(c, int):
        raise ValueError("Decimeters and centimeters must be integers")
    if d < 0 or c < 0:
        raise ValueError("Lengths cannot be negative")

def compare_measures(d1, c1, d2, c2):
    validate_length(d1, c1)
    validate_length(d2, c2)
    total_c1 = d1 * 10 + c1
    total_c2 = d2 * 10 + c2
    if total_c1 > total_c2:
        return f"{d1}dm {c1}cm"
    else:
        return f"{d2}dm {c2}cm"

if __name__ == '__main__':
    print(compare_measures(3, 5, 4, 2))