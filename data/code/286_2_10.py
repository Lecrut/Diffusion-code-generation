conversion_factors = {'yards_to_kilometers': 0.0009144}

def yards_to_kilometers(yards):
    return yards * conversion_factors['yards_to_kilometers']
if __name__ == '__main__':
    print(yards_to_kilometers(360))