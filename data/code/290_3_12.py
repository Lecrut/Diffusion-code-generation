def mg_to_g(mg):
    grams = mg / 1000.0
    return round(grams, 3)

if __name__ == '__main__':
    sample_mg_values = [500, 750, 1200]
    for mg in sample_mg_values:
        print(mg_to_g(mg))