def scale_volumes(volumes, factor):
    return [round(volume * factor, 10) for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [10.5, 20.3, 30.1, 45.75, 5.123456]
    scale_factor = 1.5
    scaled_volumes = scale_volumes(initial_volumes, scale_factor)
    print(scaled_volumes)