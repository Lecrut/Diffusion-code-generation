def liters_to_milliliters(liters):
    return liters * 1000

def format_output(value):
    return f"{value} milliliters"

if __name__ == '__main__':
    sample_liters = 2.5
    ml_value = liters_to_milliliters(sample_liters)
    formatted_string = format_output(ml_value)
    print(formatted_string)