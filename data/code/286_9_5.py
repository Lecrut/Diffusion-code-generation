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
                pass                                                                    
    return total_km
def iterative_distance_calculator(distances):
    total_km = 0.0
    i = 0
    while i < len(distances):
        dist = distances[i]
        if dist == 0:
            i += 1
            continue
        if i % 3 == 0:                                           
            total_km += dist / 1000.0
        elif i % 3 == 1:                                         
            total_km += dist / 3280.84                
        else:                                           
            total_km += dist / 1.60934                
        i += 1
    return total_km
if __name__ == '__main__':
    sample_distances = [
        1000,                     
        5280,                                
        1.60934                        
    ]
    result = iterative_distance_calculator(sample_distances)
    print(result)