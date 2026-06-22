VOLUME_SCALING_FACTOR = 2.0

def scale_volumes(volumes, factor):
    if not all(isinstance(volume, (int, float)) for volume in volumes):
        raise ValueError("All elements in volumes must be numbers.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be a number.")
    return [volume * factor for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [5.0, 10.0, 15.0]
    scaling_factor = VOLUME_SCALING_FACTOR
    scaled_volumes = scale_volumes(initial_volumes, scaling_factor)
    print(scaled_volumes)