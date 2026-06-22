def liters_to_milliliters(liters):
    return liters * 1000

def format_conversion(result):
    return f"{result:.1f} milliliters"

if __name__ == '__main__':
    input_liters = 2.5
    converted = liters_to_milliliters(input_liters)
    formatted = format_conversion(converted)
    print(formatted)