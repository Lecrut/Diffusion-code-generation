def validate_decimeters(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Decimeter value must be a non-negative integer")

def validate_centimeters(value):
    if not isinstance(value, int) or value < 0 or value >= 10:
        raise ValueError("Centimeter value must be an integer between 0 and 9")

def measure_to_cm(decimeters, centimeters):
    return decimeters * 10 + centimeters

def compare_measures(d1, c1, d2, c2):
    validate_decimeters(d1)
    validate_centimeters(c1)
    validate_decimeters(d2)
    validate_centimeters(c2)

    total_c1 = measure_to_cm(d1, c1)
    total_c2 = measure_to_cm(d2, c2)

    if total_c1 > total_c2:
        return f"{d1}dm {c1}cm"
    else:
        return f"{d2}dm {c2}cm"

if __name__ == '__main__':
    print(compare_measures(3, 5, 4, 2))