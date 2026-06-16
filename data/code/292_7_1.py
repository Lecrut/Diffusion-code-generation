def calculate_perimeter(side_lengths):
    return sum(side_lengths)
if __name__ == '__main__':
    sides1 = [3, 4, 5]
    perimeter1 = calculate_perimeter(sides1)
    print(f"Perimeter for sides {sides1}: {perimeter1}")
    sides2 = [10, 20, 30, 40]
    perimeter2 = calculate_perimeter(sides2)
    print(f"Perimeter for sides {sides2}: {perimeter2}")
    sides3 = [1, 1, 1, 1, 1]
    perimeter3 = calculate_perimeter(sides3)
    print(f"Perimeter for sides {sides3}: {perimeter3}")