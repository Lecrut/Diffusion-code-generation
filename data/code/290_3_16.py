def mg_to_g(mg):
    conversion_factor = 1 / 1000.0
    grams = mg * conversion_factor
    return round(grams, 3)

if __name__ == '__main__':
    sample_mg_values = [500, 750]
    for mg in sample_mg_values:
        print(mg_to_g(mg))