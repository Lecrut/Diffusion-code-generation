def liters_to_milliliters(liters):
    return liters * 1000

def format_output(value, unit):
    return f"{value} {unit}"

if __name__ == '__main__':
    liters_input = 1.5
    milliliters_result = liters_to_milliliters(liters_input)
    formatted_string = format_output(milliliters_result, "ml")
    print(formatted_string)