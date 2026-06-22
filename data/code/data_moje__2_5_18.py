def scale_volumes(volumes, factor):
    return [float(volume) * float(factor) for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [100, 250, 500, 1000]
    scaling_factor = 1.5
    scaled = scale_volumes(initial_volumes, scaling_factor)
    print(scaled)