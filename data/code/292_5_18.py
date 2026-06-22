BASE1 = 5
BASE2 = 7
LEG1 = 3
LEG2 = 4

def calculate_perimeter(base1, base2, leg1, leg2):
    return base1 + base2 + leg1 + leg2
if __name__ == '__main__':
    perimeter = calculate_perimeter(BASE1, BASE2, LEG1, LEG2)
    print(perimeter)