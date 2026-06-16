import sys
def convert_length(value, unit):
    if unit == "meters":
        if value > 0:
            return value * 3.28084
    elif unit == "feet":
        if value > 0:
            return value / 3.28084
    return None
if __name__ == '__main__':
    sample_length = 10
    sample_unit = "meters"
    result = convert_length(sample_length, sample_unit)
    if result is not None:
        print(f"{sample_length} {sample_unit} is equal to {result:.4f} feet")