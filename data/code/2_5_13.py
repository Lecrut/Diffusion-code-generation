def scale_volume_data(volumes, factor):
    return [float(v) * float(factor) for v in volumes]

if __name__ == '__main__':
    initial_volumes = [10.5, 20.3, 15.75, 30.0, 5.25]
    scaling_factor = 1.25
    scaled_volumes = scale_volume_data(initial_volumes, scaling_factor)
    print(scaled_volumes)