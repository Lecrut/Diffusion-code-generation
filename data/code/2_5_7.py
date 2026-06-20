def scale_volumes(volumes, factor):
    return [volume * factor for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [1.5, 2.7, 3.14, 5.0]
    scale_factor = 2.5
    scaled = scale_volumes(initial_volumes, scale_factor)
    print(scaled)