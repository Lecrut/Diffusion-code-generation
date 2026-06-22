CONVERSION_FACTOR_MG_TO_G = 0.001

def mg_to_g(mg):
    return round(mg * CONVERSION_FACTOR_MG_TO_G, 3)

if __name__ == '__main__':
    print(mg_to_g(500))
    print(mg_to_g(750))