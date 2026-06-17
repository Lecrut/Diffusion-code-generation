def validate_and_compare(d1_str: str, d2_str: str) -> bool:
    try:
        float(d1_str)
        float(d2_str)
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    distance_a = "5.0"
    distance_b = "3.7"
    if validate_and_compare(distance_a, distance_b):
        val_a = float(distance_a)
        val_b = float(distance_b)
        difference = abs(val_a - val_b)
        print(f"Difference: {difference}")