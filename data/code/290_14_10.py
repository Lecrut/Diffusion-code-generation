KG_TO_LB_FACTOR = 2.20462

def kg_to_lb(kg):
    return round(kg * KG_TO_LB_FACTOR, 2)

def lb_to_kg(lb):
    return round(lb / KG_TO_LB_FACTOR, 2)

if __name__ == '__main__':
    print(kg_to_lb(1))
    print(lb_to_kg(2.2))