def scale_volumes(volumes, factor):
    return [round(volume * factor, 10) for volume in volumes]

if __name__ == '__main__':
    sample_volumes = [10.5, 25.0, 100.123456, 0.001]
    scale_factor = 2.5
    scaled_list = scale_volumes(sample_volumes, scale_factor)
    print(scaled_list)