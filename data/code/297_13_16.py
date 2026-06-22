conversion_factor = {'pound': 0.453592, 'kg': 1 / 0.453592}

def pounds_to_kg(pounds):
    return pounds * conversion_factor['pound']

def kg_to_pounds(kg):
    return kg * conversion_factor['kg']
if __name__ == '__main__':
    print(pounds_to_kg(10))
    print(kg_to_pounds(5))