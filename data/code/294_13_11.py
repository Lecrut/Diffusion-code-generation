def calculate_equivalent_weight(mass, volume):
    density = mass / volume if volume != 0 else float('inf')
    return density
if __name__ == '__main__':
    print(calculate_equivalent_weight(100, 50))
    print(calculate_equivalent_weight(200, 0))
    print(calculate_equivalent_weight(300, 150))