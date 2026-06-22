def liters_to_milliliters(liters):
    return liters * 1000

def format_output(value, unit):
    return f"{value} {unit}"

if __name__ == '__main__':
    sample_liters = 5.5
    converted = liters_to_milliliters(sample_liters)
    message = format_output(converted, "milliliters")
    print(message)