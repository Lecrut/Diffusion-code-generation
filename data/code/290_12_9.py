def pounds_to_grams(pounds):
    return int(pounds / 0.00220462)

if __name__ == '__main__':
    print(pounds_to_grams(10))
    print(pounds_to_grams(1000))
    print(pounds_to_grams(1000000))