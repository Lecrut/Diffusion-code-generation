conversion_table = {
    "lb": 16,
}

def pounds_to_ounces(pounds):
    return int(pounds * conversion_table["lb"])

if __name__ == '__main__':
    print(pounds_to_ounces(5))
    print(pounds_to_ounces(10))