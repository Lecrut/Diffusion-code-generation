import math
def calculate_total_distance(distances):
    total_km = 0.0
    for dist in distances:
        if isinstance(dist, int) or isinstance(dist, float):
            total_km += dist / 1000.0
        elif isinstance(dist, str):
            try:
                unit = dist.strip().lower()
                value = float(dist)
                if unit == 'm':
                    total_km += value / 1000.0
                elif unit == 'ft':
                    total_km += value * 0.0003048
                elif unit == 'mi':
                    total_km += value * 1.60934
            except ValueError:
                pass
    return total_km
if __name__ == '__main__':
    sample_distances = [
        1000,          
        "5000",                      
        10,         
        2.5,         
        "10000 ft"                                                                                       
    ]
    result = calculate_total_distance(sample_distances)
    print(result)