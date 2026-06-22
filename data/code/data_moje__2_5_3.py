def scale_volumes(volumes, factor):
    return [float(volume) * float(factor) for volume in volumes]

if __name__ == '__main__':
    sample_volumes = [10.5, 20.25, 30.75, 40.0]
    scale_factor = 2.5
    result = scale_volumes(sample_volumes, scale_factor)
    print(result)