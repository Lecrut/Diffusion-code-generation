CONVERSION_FACTOR_MG_TO_G = 1000.0

def mg_to_g(mg):
    return round(mg / CONVERSION_FACTOR_MG_TO_G, 3)

if __name__ == '__main__':
    sample_mg_values = [500, 750]
    for mg in sample_mg_values:
        print(mg_to_g(mg))