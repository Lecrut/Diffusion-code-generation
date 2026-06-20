def scale_volume_data(volumes, factor):
    return [v * factor for v in volumes]

if __name__ == '__main__':
    initial_volumes = [100.5, 250.75, 50.0, 1000.123]
    scaling_factor = 2.5
    scaled_volumes = scale_volume_data(initial_volumes, scaling_factor)
    print(scaled_volumes)