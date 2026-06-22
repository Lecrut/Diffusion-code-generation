LITERS_TO_MILLILITERS = 1000

def liters_to_milliliters(liters):
    return liters * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_values = [0, 1, 0.5, -2.5, 1000]
    for value in sample_values:
        result = liters_to_milliliters(value)
        print(f"{value} liters = {result} milliliters")