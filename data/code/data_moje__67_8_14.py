def convert_liters_to_milliliters(liters):
    return liters * 1000

def format_output(value, unit):
    return f"{value} {unit}"

if __name__ == '__main__':
    input_liters = 2.5
    milliliters = convert_liters_to_milliliters(input_liters)
    result_string = format_output(milliliters, "mL")
    print(result_string)