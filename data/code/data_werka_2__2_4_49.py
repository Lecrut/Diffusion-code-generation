def scale_volumes(volumes, factor):
    scaled_data = []
    for volume in volumes:
        if not isinstance(volume, (int, float)):
            raise ValueError("All elements in volumes must be numbers.")
        if not isinstance(factor, (int, float)):
            raise ValueError("Factor must be a number.")
        scaled_value = float(volume) * float(factor)
        scaled_data.append(scaled_value)
    return scaled_data

if __name__ == '__main__':
    initial_volumes = [0.5, 1.2, 2.8, 3.4]
    scaling_factor = 1.5
    result = scale_volumes(initial_volumes, scaling_factor)
    print(result)