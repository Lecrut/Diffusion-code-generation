def scale_volumes(volumes, factor):
    return [v * factor for v in volumes]

if __name__ == '__main__':
    initial_volumes = [1.5, 2.0, 3.75, 0.5]
    scale_factor = 2.0
    scaled = scale_volumes(initial_volumes, scale_factor)
    print(scaled)