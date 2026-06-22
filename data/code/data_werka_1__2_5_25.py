def scale_volumes(volumes, factor):
    return [volume * factor for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [1.5, 2.3, 3.7, 4.1]
    scale_factor = 2.0
    scaled_volumes = scale_volumes(initial_volumes, scale_factor)
    print(scaled_volumes)