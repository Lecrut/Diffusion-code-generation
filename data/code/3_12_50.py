def celsius_to_kelvin(celsius):
    kelvin_offset = 273.15
    return celsius + kelvin_offset

if __name__ == '__main__':
    sample_temperatures = [
        {'label': 'Freezing Point', 'celsius': 0},
        {'label': 'Boiling Point', 'celsius': 100},
        {'label': 'Absolute Zero', 'celsius': -273.15},
        {'label': 'Human Body Temperature', 'celsius': 37}
    ]
    
    for sample in sample_temperatures:
        kelvin_value = celsius_to_kelvin(sample['celsius'])
        print(f"{sample['label']}: {sample['celsius']}C is {kelvin_value}K")