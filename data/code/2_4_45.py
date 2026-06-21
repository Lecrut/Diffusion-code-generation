def scale_volumes(volumes, factor):
    if not all(isinstance(volume, (int, float)) for volume in volumes):
        raise ValueError("All elements in volumes must be numbers.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be a number.")
    
    scaled = []
    for volume in volumes:
        scaled_volume = volume * factor
        scaled.append(scaled_volume)
    
    return scaled

if __name__ == '__main__':
    initial_volumes = [5.0, 10.0, 15.0]
    scaling_factor = 3.0
    result = scale_volumes(initial_volumes, scaling_factor)
    print(result)