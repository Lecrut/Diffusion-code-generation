CONVERSION_TABLE = {'pounds': 1 / 0.00220462}

def pounds_to_grams(pounds):
    return int(pounds * CONVERSION_TABLE['pounds'])

if __name__ == '__main__':
    print(pounds_to_grams(100))
    print(pounds_to_grams(5000))