def scale_volumes(volumes, factor):
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be a number.")
    return [float(volume) * factor for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [5.5, 6.3, 7.8]
    scaling_factor = 1.2
    scaled_volumes = scale_volumes(initial_volumes, scaling_factor)
    print(scaled_volumes)