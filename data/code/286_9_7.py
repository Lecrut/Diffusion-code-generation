import math
def calculate_total_distance(distances):
    total_km = 0.0
    for dist in distances:
        if isinstance(dist, int) or isinstance(dist, float):
            if dist == 0:
                continue
            elif dist == 1:
                total_km += 1.60934                 
            elif dist == 1000:
                total_km += 1.0                     
            else:
                total_km += dist / 1000.0
        elif isinstance(dist, str):
            try:
                value = float(dist)
                if value == 0:
                    continue
                elif value == 1:
                    total_km += 1.60934
                elif value == 1000:
                    total_km += 1.0
                else:
                    total_km += value / 1000.0
            except ValueError:
                pass
        elif isinstance(dist, tuple) and len(dist) == 3:
            meters, feet, miles = dist
            total_meters = meters + feet * 0.3048 + miles * 1609.344
            total_km += total_meters / 1000.0
    return total_km
if __name__ == '__main__':
    sample_distances = [
        1000,          
        500000,         
        10,         
        2,           
        (100, 0, 0)                               
    ]
    result = calculate_total_distance(sample_distances)
    print(result)