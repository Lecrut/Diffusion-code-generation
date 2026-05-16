def scale_volumes(volumes, factor):
    scaled_volumes = []
    for volume in volumes:
        scaled_volume = volume * factor
        scaled_volumes.append(scaled_volume)
    return scaled_volumes
if __name__ == '__main__':
    initial_volumes = [1.0, 2.5, 3.14159, 10.0]
    scaling_factor = 1.5
    result = scale_volumes(initial_volumes, scaling_factor)
    print(result)