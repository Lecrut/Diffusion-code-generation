def scale_volumes(volumes, factor):
    return [volume * factor for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [10.0, 20.5, 30.75]
    scaling_factor = 2.5
    scaled_volumes = scale_volumes(initial_volumes, scaling_factor)
    print(scaled_volumes)