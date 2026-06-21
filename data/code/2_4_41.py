def scale_volumes(volumes, factor):
    scaled = []
    for volume in volumes:
        if not isinstance(volume, (int, float)):
            raise ValueError("All elements in volumes must be numbers.")
        if not isinstance(factor, (int, float)):
            raise ValueError("Factor must be a number.")
        scaled.append(float(volume) * float(factor))
    return scaled

if __name__ == '__main__':
    initial_volumes = [5.0, 10.0, 15.0]
    scaling_factor = 3.0
    result = scale_volumes(initial_volumes, scaling_factor)
    print(result)