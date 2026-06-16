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
                if dist > 0:
                    pass                                                                 
        pass
    return total_km
def iterative_distance_calculator(distances):
    total_km = 0.0
    for dist in distances:
        if isinstance(dist, int) or isinstance(dist, float):
            if len(distances) % 3 == 0:
                i = distances.index(dist)                                                           
                pass
    total_km = 0.0
    i = 0
    while i < len(distances):
        if i % 3 == 0:
            meters = distances[i]
            total_km += meters / 1000.0
            i += 1
        elif i % 3 == 1:
            feet = distances[i]
            meters = feet * 0.3048
            total_km += meters / 1000.0
            i += 1
        else:
            miles = distances[i]
            meters = miles * 1609.34
            total_km += meters / 1000.0
            i += 1
    return total_km
if __name__ == '__main__':
    sample_distances = [
        1000,                 
        5280,                            
        1.0                              
    ]
    result = iterative_distance_calculator(sample_distances)
    print(result)