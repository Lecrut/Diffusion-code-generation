conversion_table = {'g': 0.035274}

def grams_to_ounces(grams: float) -> str:
    ounces = grams * conversion_table['g']
    return f'{ounces:.2f} oz'
if __name__ == '__main__':
    print(grams_to_ounces(100))