def pounds_to_grams(pounds):
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Invalid input: pounds must be a non-negative number")
    return int(pounds / 0.00220462)

if __name__ == '__main__':
    print(pounds_to_grams(100))
    print(pounds_to_grams(5000))