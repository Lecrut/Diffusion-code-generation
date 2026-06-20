def scale_volumes(volumes, factor):
    return [v * float(factor) for v in volumes]

if __name__ == '__main__':
    initial_volumes = [10, 25, 37.5, 50]
    scale_factor = 1.25
    scaled_volumes = scale_volumes(initial_volumes, scale_factor)
    print(scaled_volumes)