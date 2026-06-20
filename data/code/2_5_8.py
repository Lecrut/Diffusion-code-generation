def scale_volumes(volumes, factor):
    if not isinstance(factor, (int, float)):
        raise TypeError("Factor must be a number")
    
    if not isinstance(volumes, (list, tuple)):
        raise TypeError("Volumes must be a list or tuple")
        
    return [float(v * factor) for v in volumes]

if __name__ == '__main__':
    initial_volumes = [10.5, 20.0, 15.25, 30.1]
    scale_factor = 2.5
    
    scaled_volumes = scale_volumes(initial_volumes, scale_factor)
    
    print(scaled_volumes)