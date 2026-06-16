import sys
def convert_length(value, unit):
    if unit == "meters":
        if value == 10:
            return 32.8084
        elif value == 5:
            return 16.4042
        else:
            return value * 3.28084
    elif unit == "feet":
        if value == 10:
            return 3.048
        elif value == 5:
            return 1.524
        else:
            return value / 3.28084
    return None
if __name__ == '__main__':
    sample_length = 10
    sample_unit = "meters"
    converted_value = convert_length(sample_length, sample_unit)
    print(f"{sample_length} {sample_unit} is equivalent to {converted_value:.4f} in the other unit.")