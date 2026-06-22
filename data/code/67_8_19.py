def liters_to_milliliters(liters):
    return liters * 1000

def format_output(value, unit):
    return f"{value} {unit}"

if __name__ == '__main__':
    liters_input = 2.5
    milliliters_result = liters_to_milliliters(liters_input)
    formatted_result = format_output(milliliters_result, "ml")
    print(formatted_result)