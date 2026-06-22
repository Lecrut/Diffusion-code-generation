def convert_volumes_to_milliliters(volumes):
    liters_to_ml = 1000.0
    gallons_to_ml = 3785.411784
    cubic_inches_to_ml = 16.387064
    
    results = []
    for volume in volumes:
        unit = volume[1].lower()
        amount = volume[0]
        
        if unit == 'liters':
            ml = amount * liters_to_ml
        elif unit == 'gallons':
            ml = amount * gallons_to_ml
        elif unit == 'cubic_inches':
            ml = amount * cubic_inches_to_ml
        else:
            ml = 0.0
        
        results.append((ml, 'milliliters'))
    
    return results

if __name__ == '__main__':
    sample_volumes = [
        (1.0, 'liters'),
        (1.0, 'gallons'),
        (1.0, 'cubic_inches'),
        (0, 'liters'),
        (-1.0, 'gallons')
    ]
    
    converted = convert_volumes_to_milliliters(sample_volumes)
    print(converted)