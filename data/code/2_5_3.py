def scale_volumes(volumes, factor):
    scaled_volumes = []
    for volume in volumes:
        scaled_volume = volume * factor
        scaled_volumes.append(scaled_volume)
    return scaled_volumes
if __name__ == '__main__':
    initial_volumes = [1.5, 2.75, 3.0, 4.2]
    scaling_factor = 1.5
    scaled_result = scale_volumes(initial_volumes, scaling_factor)
    print(scaled_result)