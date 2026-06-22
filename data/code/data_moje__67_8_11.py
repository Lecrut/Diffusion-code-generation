def convert_liters_to_milliliters(liters):
    return liters * 1000

def format_output(value, unit):
    return f"{value} {unit}"

if __name__ == "__main__":
    sample_liters = 2.5
    result_ml = convert_liters_to_milliliters(sample_liters)
    formatted_string = format_output(result_ml, "milliliters")
    print(formatted_string)