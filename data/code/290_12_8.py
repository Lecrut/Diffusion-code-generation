CONVERSION_FACTOR = 0.00220462

def validate_pounds(pounds):
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Pounds must be a non-negative number")

def pounds_to_grams(pounds):
    validate_pounds(pounds)
    return int(pounds / CONVERSION_FACTOR)

if __name__ == '__main__':
    print(pounds_to_grams(100))
    print(pounds_to_grams(5000))