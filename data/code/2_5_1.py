def scale_volumes(volumes, factor):
    return [volume * factor for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [100.5, 200.75, 300.25, 400.0]
    scale_factor = 1.5
    scaled = scale_volumes(initial_volumes, scale_factor)
    print(scaled)