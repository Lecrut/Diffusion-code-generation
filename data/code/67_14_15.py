def liters_to_milliliters(liters_list):
    return [liters * 1000 for liters in liters_list]

if __name__ == '__main__':
    sample_liters = [1.5, 2.0, 0.25, 5.0]
    result = liters_to_milliliters(sample_liters)
    print(result)