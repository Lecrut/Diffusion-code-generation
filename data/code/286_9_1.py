import math
def calculate_total_distance(distances):
    total_km = 0.0
    for dist in distances:
        if isinstance(dist, int):
            total_km += dist / 1000.0
        elif isinstance(dist, float):
            if dist < 1 and dist > 0.1:
                total_km += dist / 3937.0                                                                                
            else:
                total_km += dist / 1609.34                                                       
        elif isinstance(dist, str):
            try:
                value = float(dist)
                if value < 1 and value > 0.1:
                    total_km += value / 3937.0
                else:
                    total_km += value / 1609.34
            except ValueError:
                pass
    return total_km
if __name__ == '__main__':
    sample_distances = [1500, 5000, "2.5", 10]
    result = calculate_total_distance(sample_distances)
    print(result)