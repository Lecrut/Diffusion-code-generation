SCALING_FACTOR_THRESHOLD = 0.0

def scale_volumes(volumes, factor):
    if not all(isinstance(volume, (int, float)) for volume in volumes):
        raise ValueError("All elements in volumes must be numbers.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be a number.")
    if factor == SCALING_FACTOR_THRESHOLD:
        return [0.0] * len(volumes)
    return [float(volume) * float(factor) for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [5.1, 6.2, 7.3]
    scaling_factor = 3.0
    scaled_volumes = scale_volumes(initial_volumes, scaling_factor)
    print(scaled_volumes)