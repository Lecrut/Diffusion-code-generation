CONVERSION_FACTOR = 16

def pounds_to_ounces(pounds):
    return int(pounds * CONVERSION_FACTOR)

if __name__ == '__main__':
    print(pounds_to_ounces(5))
    print(pounds_to_ounces(10))