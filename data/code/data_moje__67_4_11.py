def liters_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    sample_values = [1.0, 0.5, 2.5, 0.1, 10.0]
    for liters in sample_values:
        print(liters_to_milliliters(liters))