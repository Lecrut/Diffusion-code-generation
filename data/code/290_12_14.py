CONVERSION_FACTOR = 0.00220462

def pounds_to_grams(pounds):
    grams = pounds / CONVERSION_FACTOR
    return int(grams)

if __name__ == '__main__':
    sample_pounds1 = 150
    sample_pounds2 = 7500
    print(f"{sample_pounds1} pounds is {pounds_to_grams(sample_pounds1)} grams")
    print(f"{sample_pounds2} pounds is {pounds_to_grams(sample_pounds2)} grams")