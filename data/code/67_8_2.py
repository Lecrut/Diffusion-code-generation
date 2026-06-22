def convert_liters_to_milliliters(liters):
    return liters * 1000

def format_result(liters, milliliters):
    return f"{liters} liters is {milliliters} milliliters"

if __name__ == '__main__':
    input_liters = 2.5
    ml_result = convert_liters_to_milliliters(input_liters)
    output_string = format_result(input_liters, ml_result)
    print(output_string)