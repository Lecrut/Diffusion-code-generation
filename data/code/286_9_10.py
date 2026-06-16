import math
def calculate_total_distance(distances):
    total_distance = 0.0
    for dist in distances:
        if isinstance(dist, int) or isinstance(dist, float):
            total_distance += float(dist)
        elif isinstance(dist, str):
            try:
                unit = dist.strip().lower()
                value = float(dist)
                if unit == 'meters':
                    total_distance += value / 1000.0
                elif unit == 'feet':
                    total_distance += value * 0.003048
                elif unit == 'miles':
                    total_distance += value * 1609.34
                else:
                    raise ValueError("Unknown unit")
            except ValueError:
                pass
        else:
            pass
    return total_distance
if __name__ == '__main__':
    sample_distances = [
        100,          
        "5000",        
        2.5,         
        100000,         
        "10",         
        3000000         
    ]
    result = calculate_total_distance(sample_distances)
    print(result)