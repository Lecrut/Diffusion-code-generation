def convert_distance(distance, target_unit):
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    
    if target_unit == 'meters':
        return distance
    elif target_unit == 'kilometers':
        if distance == 0:
            return 0.0
        return distance / 1000.0
    elif target_unit == 'centimeters':
        if distance == 0:
            return 0.0
        return distance * 100.0
    elif target_unit == 'millimeters':
        if distance == 0:
            return 0.0
        return distance * 1000.0
    elif target_unit == 'feet':
        if distance == 0:
            return 0.0
        return distance / 0.3048
    elif target_unit == 'miles':
        if distance == 0:
            return 0.0
        return distance / 1609.344
    elif target_unit == 'inches':
        if distance == 0:
            return 0.0
        return distance / 0.0254
    else:
        raise ValueError(f"Unknown target unit: {target_unit}")

if __name__ == '__main__':
    result = convert_distance(1000, 'kilometers')
    print(result)