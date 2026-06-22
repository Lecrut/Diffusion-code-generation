def convert_liters_to_milliliters(liters):
    return liters * 1000

def format_output(value):
    return f"{value} milliliters"

if __name__ == '__main__':
    sample_liters = 5.5
    converted_value = convert_liters_to_milliliters(sample_liters)
    formatted_string = format_output(converted_value)
    print(formatted_string)