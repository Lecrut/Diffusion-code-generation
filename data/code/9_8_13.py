import numpy as np

def convert_volumes(volumes_liters):
    volumes_cubic_meters = volumes_liters / 1000.0
    volumes_gallons = volumes_liters * 0.264172
    volumes_ml = volumes_liters * 1000.0
    return volumes_cubic_meters, volumes_gallons, volumes_ml

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 5.0, 10.0, 50.0, 100.0])
    cubic_meters, gallons, ml = convert_volumes(sample_volumes)
    print(cubic_meters)
    print(gallons)
    print(ml)