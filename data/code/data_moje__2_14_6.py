def convert_volumes_to_milliliters(volumes):
    liters_to_ml = 1000.0
    gallons_to_ml = 3785.411784
    cubic_inches_to_ml = 16.387064
    
    results = []
    for volume in volumes:
        unit = volume[0]
        value = volume[1]
        
        if unit == 'liters':
            ml = value * liters_to_ml
        elif unit == 'gallons':
            ml = value * gallons_to_ml
        elif unit == 'cubic_inches':
            ml = value * cubic_inches_to_ml
        else:
            raise ValueError(f"Unknown unit: {unit}")
            
        results.append(ml)
    
    return results

if __name__ == '__main__':
    sample_volumes = [
        ('liters', 1),
        ('gallons', 0),
        ('cubic_inches', -1),
        ('liters', 2.5)
    ]
    
    converted = convert_volumes_to_milliliters(sample_volumes)
    print(converted)