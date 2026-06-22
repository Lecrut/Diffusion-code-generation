def convert_liters_to_milliliters(liters):
    return liters * 1000

def format_output(value):
    return f"{value} ml"

if __name__ == '__main__':
    liters_input = 5
    result_ml = convert_liters_to_milliliters(liters_input)
    formatted_result = format_output(result_ml)
    print(formatted_result)