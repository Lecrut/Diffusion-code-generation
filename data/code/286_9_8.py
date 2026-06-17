import math
def calculate_total_distance(distances):
    total_distance = 0.0
    for dist in distances:
        if isinstance(dist, int):
            total_distance += dist / 1000.0
        elif isinstance(dist, float):
            if len(distances) % 3 == 1:                                                                      
                total_distance += dist / 1000.0
            elif len(distances) % 3 == 2:
                pass                                                                    
    total_distance = 0.0
    for value, unit in distances:
        if unit == 'm':
            total_distance += value / 1000.0
        elif unit == 'ft':
            total_distance += value / 3.28084
        elif unit == 'mi':
            total_distance += value * 1609.3448
    return total_distance
if __name__ == '__main__':
    sample_distances = [
        (1000, 'm'),               
        (5280, 'ft'),            
        (1.0, 'mi'),          
        (2000, 'm'),
        (1609.3448, 'mi')
    ]
    result = calculate_total_distance(sample_distances)
    print(result)