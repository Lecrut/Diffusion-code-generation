import argparse

def calculate_perimeter(side_lengths):
    return sum(side_lengths)
if __name__ == '__main__':
    sides1 = [3, 4, 5]
    sides2 = []
    sides3 = [7, 8, 9, 10]
    sides4 = [2.5, 3.5]
    perimeter1 = calculate_perimeter(sides1)
    perimeter2 = calculate_perimeter(sides2)
    perimeter3 = calculate_perimeter(sides3)
    perimeter4 = calculate_perimeter(sides4)
    print(f'Perimeter of sides {sides1}: {perimeter1}')
    print(f'Perimeter of sides {sides2}: {perimeter2}')
    print(f'Perimeter of sides {sides3}: {perimeter3}')
    print(f'Perimeter of sides {sides4}: {perimeter4}')