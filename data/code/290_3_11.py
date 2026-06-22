CONVERSION_FACTOR = 1 / 1000.0

def mg_to_g(mg):
    return round(mg * CONVERSION_FACTOR, 3)

if __name__ == '__main__':
    sample_mg_values = [500, 750]
    for mg in sample_mg_values:
        print(mg_to_g(mg))