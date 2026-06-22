def validate_milligrams(mg):
    if not isinstance(mg, (int, float)) or mg < 0:
        raise ValueError("Milligram value must be a non-negative number")

def convert_to_grams(mg):
    validate_milligrams(mg)
    return round(mg / 1000.0, 3)

if __name__ == '__main__':
    sample_milligrams = [500, 750]
    for mg in sample_milligrams:
        print(convert_to_grams(mg))