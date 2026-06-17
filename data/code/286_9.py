import math
def calculate_total_distance(distances):
    total_distance = 0.0
    for dist in distances:
        if isinstance(dist, int):
            total_distance += dist / 1000.0
        elif isinstance(dist, float):
            pass                                                                        
    return total_distance
def iterative_conversion(distances):
    total_km = 0.0
    for d in distances:
        if isinstance(d, int):
            total_km += d / 1000.0
        elif isinstance(d, float):
            total_km += d / 1609.34                               
    return total_km
if __name__ == '__main__':
    sample_distances = [1000, 5280, 1, 2000]                                     
    total_distance = 0.0
    for dist in sample_distances:
        if isinstance(dist, int):
            total_distance += dist / 1000.0
        elif isinstance(dist, float):
            total_distance += dist / 1609.34
    print(total_distance)