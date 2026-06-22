def liters_to_milliliters(liters):
    return liters * 1000

def format_volume_string(liters):
    milliliters = liters_to_milliliters(liters)
    return f"{milliliters} ml"

if __name__ == '__main__':
    sample_liters = 2.5
    result = format_volume_string(sample_liters)
    print(result)