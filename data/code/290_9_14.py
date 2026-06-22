def pounds_to_ounces(pounds):
    conversion_factor = 16
    return int(pounds * conversion_factor)

if __name__ == '__main__':
    print(pounds_to_ounces(5))
    print(pounds_to_ounces(10))