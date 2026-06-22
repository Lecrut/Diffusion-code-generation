def scale_volumes(volumes, factor):
    if not all(isinstance(volume, (int, float)) for volume in volumes):
        raise ValueError("All elements in volumes must be numbers.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be a number.")
    
    return [volume * factor for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [1.2, 3.4, 5.6, 7.8]
    scaling_factor = 1.25
    scaled_volumes = scale_volumes(initial_volumes, scaling_factor)
    print(scaled_volumes)