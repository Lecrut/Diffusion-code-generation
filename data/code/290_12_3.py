CONVERSION_FACTOR = 0.00220462

def pounds_to_grams(pounds):
    return int(pounds / CONVERSION_FACTOR)

if __name__ == '__main__':
    print(pounds_to_grams(100))
    print(pounds_to_grams(5000))