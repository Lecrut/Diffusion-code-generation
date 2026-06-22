def liters_to_milliliters(liters_list):
    return [liters * 1000 for liters in liters_list]

if __name__ == '__main__':
    sample_liters = [0.5, 1.0, 2.5, 10.0]
    result = liters_to_milliliters(sample_liters)
    print(result)