CONVERSION_FACTOR = {
    'kg_to_lb': 2.20462,
    'lb_to_kg': 1 / 2.20462
}

def kg_to_lb(kg):
    return round(kg * CONVERSION_FACTOR['kg_to_lb'], 2)

def lb_to_kg(lb):
    return round(lb * CONVERSION_FACTOR['lb_to_kg'], 2)

if __name__ == '__main__':
    print(kg_to_lb(1))
    print(lb_to_kg(2.2))