def scale_volumes(volumes, factor):
    return [float(volume) * float(factor) for volume in volumes]

if __name__ == '__main__':
    initial_volumes = [1.5, 2.0, 3.25, 4.5, 5.0]
    scaling_factor = 2.5
    scaled = scale_volumes(initial_volumes, scaling_factor)
    print(scaled)