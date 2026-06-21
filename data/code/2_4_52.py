SCALING_PRECISION = 10

def scale_volumes(volumes, factor):
    if not all(isinstance(volume, (int, float)) for volume in volumes):
        raise ValueError("All elements in volumes must be numbers.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be a number.")
    
    scaled_volumes = []
    for volume in volumes:
        scaled_volume = round(volume * factor, SCALING_PRECISION)
        scaled_volumes.append(scaled_volume)
    
    return scaled_volumes

if __name__ == '__main__':
    initial_volumes = [1.5, 2.3, 3.7, 4.1]
    scaling_factor = 2.0
    scaled_volumes = scale_volumes(initial_volumes, scaling_factor)
    print(scaled_volumes)