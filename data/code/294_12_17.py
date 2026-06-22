def calculate_equivalent_weight(density, quantity):
    return density * quantity

if __name__ == '__main__':
    substances = [
        {'density': 2.5, 'quantity': 3},
        {'density': 1.0, 'quantity': 4},
        {'density': 3.0, 'quantity': 2}
    ]
    
    for substance in substances:
        weight = calculate_equivalent_weight(substance['density'], substance['quantity'])
        print(f"Substance with density {substance['density']} and quantity {substance['quantity']} has an equivalent weight of {weight}")