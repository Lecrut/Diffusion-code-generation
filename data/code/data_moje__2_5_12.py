def scale_volumes(volumes, factor):
    return [v * factor for v in volumes]

if __name__ == '__main__':
    initial_volumes = [10.0, 20.5, 30.123456789]
    scale_factor = 2.5
    result = scale_volumes(initial_volumes, scale_factor)
    print(result)