def pounds_to_kilograms(pounds):
    kilograms = pounds * 0.453592
    return "{:.2f}".format(kilograms)

if __name__ == '__main__':
    print(pounds_to_kilograms(10))
    print(pounds_to_kilograms(20))