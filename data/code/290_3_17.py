def mg_to_g(mg):
    try:
        grams = mg / 1000.0
        return round(grams, 3)
    except TypeError:
        raise ValueError("Invalid input: expected a number")

if __name__ == '__main__':
    sample_mg_values = [500, 750]
    for mg in sample_mg_values:
        print(mg_to_g(mg))