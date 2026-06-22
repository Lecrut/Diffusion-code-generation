VOLUME_SCALE_FACTOR = 2.0

def scale_volumes(volumes, factor=VOLUME_SCALE_FACTOR):
    if not all(isinstance(volume, (int, float)) for volume in volumes):
        raise ValueError("All elements in volumes must be numbers.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be a number.")
    return [float(volume) * float(factor) for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [1.5, 2.3, 3.7, 4.1]
    scaled_volumes = scale_volumes(initial_volumes)
    print(scaled_volumes)