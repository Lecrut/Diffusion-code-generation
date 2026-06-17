import sys
def kg_to_g(kg):
    return kg * 1000
def g_to_kg(g):
    return g / 1000
def kg_to_lb(kg):
    return kg * 2.20462
def lb_to_kg(lb):
    return lb / 2.20462
def convert_mass():
    kg = 5
    g = 500
    lb = 150
    print("--- Mass Conversion Example ---")
    print(f"Initial values: kg={kg}, g={g}, lb={lb}\n")
    print("Conversion Results:")
    print(f"Kilograms to Grams: {kg} kg is equal to {kg_to_g(kg)} g")
    print(f"Grams to Kilograms: {g} g is equal to {g_to_kg(g)} kg")
    print(f"Kilograms to Pounds: {kg} kg is equal to {kg_to_lb(kg)} lb")
    print(f"Pounds to Kilograms: {lb} lb is equal to {lb_to_kg(lb)} kg")
if __name__ == '__main__':
    convert_mass()