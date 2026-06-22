def convert_to_milliliters(volumes_liters):
    return [vol * 1000 for vol in volumes_liters]

if __name__ == '__main__':
    sample_liters = [1.5, 2.0, 0.5]
    result = convert_to_milliliters(sample_liters)
    print(result)