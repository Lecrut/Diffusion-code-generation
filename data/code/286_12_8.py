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
    feet = convert_length(sample_length, sample_unit)
    print(f"Sample Length: {sample_length} {sample_unit}")
    if feet is not None:
        print(f"Equivalent in the other unit: {feet:.4f} feet")
    else:
        print("Error in conversion.")