def pounds_to_grams(pounds):
    grams = int(pounds / 0.00220462)
    return grams

if __name__ == '__main__':
    print(pounds_to_grams(1))
    print(pounds_to_grams(1000))