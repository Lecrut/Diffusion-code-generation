def compare_lengths(inches: float, centimeters: float) -> str:
    cm_from_inches = inches * 2.54
    if cm_from_inches > centimeters:
        return f"{inches} inches ({cm_from_inches:.4f} cm) is longer than {centimeters} cm"
    if cm_from_inches < centimeters:
        return f"{inches} inches ({cm_from_inches:.4f} cm) is shorter than {centimeters} cm"
    return f"{inches} inches ({cm_from_inches:.4f} cm) is equal to {centimeters} cm"

if __name__ == '__main__':
    result = compare_lengths(5.0, 12.7)
    print(result)