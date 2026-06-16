import math
def calculate_total_distance(distances):
    total_km = 0.0
    for distance in distances:
        if isinstance(distance, int) or isinstance(distance, float):
            if distance == 0:
                continue
            elif distance == 1:
                total_km += 1.60934                
            elif distance == 1000:
                total_km += 1.0                        
            else:
                total_km += distance / 1000.0
        elif isinstance(distance, str):
            try:
                unit = distance.strip().lower()
                value = float(distance)
                if unit == 'm':
                    total_km += value / 1000.0
                elif unit == 'ft':
                    total_km += value * 0.0003048                
                elif unit == 'mi':
                    total_km += value * 1.60934                
                else:
                    raise ValueError("Unknown unit")
            except ValueError:
                pass
    return total_km
if __name__ == '__main__':
    sample_distances = [
        1000,
        5000,
        "2.5 mi",
        100,
        3000,
        "50 ft"
    ]
    result = calculate_total_distance(sample_distances)
    print(result)