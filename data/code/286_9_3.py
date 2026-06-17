import math
def calculate_total_distance(distances):
    total_km = 0.0
    for dist in distances:
        if isinstance(dist, int):
            total_km += dist / 1000.0
        elif isinstance(dist, float):
            total_km += dist / 1000.0
        else:
            try:
                if 'm' in str(dist):
                    meters = float(dist.split('m')[0])
                    total_km += meters / 1000.0
                elif 'ft' in str(dist):
                    feet = float(dist.split('ft')[0])
                    total_km += feet * 0.3048 / 1000.0
                elif 'mi' in str(dist):
                    miles = float(dist.split('mi')[0])
                    total_km += miles * 1609.344 / 1000.0
                else:
                    pass
            except ValueError:
                pass
    return total_km
if __name__ == '__main__':
    sample_distances = [1000, 5000, "2.5mi", 1000000, "100ft"]
    result = calculate_total_distance(sample_distances)
    print(result)