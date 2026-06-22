def calculate_weight(density, volume):
    return density * volume
if __name__ == '__main__':
    density_iron = 7850
    volume_iron = 0.1
    weight_iron = calculate_weight(density_iron, volume_iron)
    print(weight_iron)
    density_water = 1000
    volume_water = 0.5
    weight_water = calculate_weight(density_water, volume_water)
    print(weight_water)