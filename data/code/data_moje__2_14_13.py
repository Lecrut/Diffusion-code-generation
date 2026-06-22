def convert_volumes_to_ml(volumes):
    result = []
    for v in volumes:
        if v == 0:
            result.append(0.0)
            continue
        if not isinstance(v, (int, float)):
            raise TypeError("Volume values must be numeric.")
        
        unit = str(v).lower().split(' ')[-1] if ' ' in str(v) else ''
        val = float(str(v).split(' ')[0]) if ' ' in str(v) else float(str(v))
        
        if val < 0:
            val = abs(val)
            
        if unit == 'liters' or unit == 'liter':
            converted = val * 1000.0
        elif unit == 'gallons' or unit == 'gallon':
            converted = val * 3785.41
        elif unit == 'cubic_inches' or unit == 'cubic_inch':
            converted = val * 16.387064
        else:
            if isinstance(v, tuple):
                val, unit = v
                if val < 0:
                    val = abs(val)
                if unit == 'liters' or unit == 'liter':
                    converted = val * 1000.0
                elif unit == 'gallons' or unit == 'gallon':
                    converted = val * 3785.41
                elif unit == 'cubic_inches' or unit == 'cubic_inch':
                    converted = val * 16.387064
                else:
                    raise ValueError(f"Unsupported unit: {unit}")
            else:
                raise ValueError(f"Unit must be specified for value: {v}")
        
        if v < 0:
            result.append(-converted)
        else:
            result.append(converted)
    return result

if __name__ == '__main__':
    samples = [
        (1.0, 'liters'),
        (2.5, 'gallons'),
        (100, 'cubic_inches'),
        (0, 'liters'),
        (-1.0, 'liters')
    ]
    print(convert_volumes_to_ml(samples))