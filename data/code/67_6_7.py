UNITS = {'L': 1000, 'mL': 1}
def liters_to_milliliters(value):
    return value * UNITS['L']
if __name__ == '__main__':
    print(liters_to_milliliters(10))