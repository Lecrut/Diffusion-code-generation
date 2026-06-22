def scale_volume_data(volumes, factor):
    return [volume * factor for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [10.5, 25.3, 7.8, 100.0, 0.25]
    scaling_factor = 1.5
    scaled_volumes = scale_volume_data(initial_volumes, scaling_factor)
    print(scaled_volumes)