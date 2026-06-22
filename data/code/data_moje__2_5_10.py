def scale_volumes(volumes, factor):
    return [v * factor for v in volumes]

if __name__ == '__main__':
    initial_volumes = [1.5, 2.0, 3.75]
    scaling_factor = 2.5
    scaled = scale_volumes(initial_volumes, scaling_factor)
    print(scaled)