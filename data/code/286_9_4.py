import math
def calculate_total_distance(distances):
    total_km = 0.0
    for dist in distances:
        if isinstance(dist, int):
            total_km += dist / 1000.0
        elif isinstance(dist, float):
            pass                                                            
    return total_km
def iterative_distance_calculator(distances):
    total_km = 0.0
    for dist in distances:
        if isinstance(dist, int):
            total_km += dist / 1000.0
        elif isinstance(dist, float):
            total_km += dist / 1000.0                                                                              
        else:
            pass
    return total_km
if __name__ == '__main__':
    sample_distances = [1000, 500000, 10, 26.67]                                                  
    def final_calculator(distances):
        total_km = 0.0
        for dist in distances:
            if isinstance(dist, int):
                total_km += dist / 1000.0
            elif isinstance(dist, float):
                if dist < 50.0:
                    total_km += dist * 0.3048                  
                else:
                    total_km += dist * 1609.34                   
            else:
                pass
        return total_km
    result = final_calculator(sample_distances)
    print(result)