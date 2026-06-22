def convert_to_milliliters(liters_list):
    return list(map(lambda x: x * 1000, liters_list))

if __name__ == '__main__':
    sample_liters = [1.5, 2.0, 0.75, 3.25]
    result = convert_to_milliliters(sample_liters)
    print(result)