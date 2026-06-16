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
    meters = sample_length
    feet = 0
    if sample_unit == "meters":
        feet = sample_length * 3.28084
    elif sample_unit == "feet":
        meters = sample_length / 3.28084
    print(f"Sample Length: {sample_length} {sample_unit}")
    if sample_unit == "meters":
        print(f"Equivalent in feet: {feet:.4f}")
    elif sample_unit == "feet":
        print(f"Equivalent in meters: {meters:.4f}")