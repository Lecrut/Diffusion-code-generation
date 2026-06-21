def find_max_min_volumes(volumes):
    if not isinstance(volumes, list) or not all(isinstance(v, (int, float)) for v in volumes):
        raise ValueError("Input must be a list of numbers.")
    
    if len(volumes) == 0:
        return None, None
    
    max_volume = float('-inf')
    min_volume = float('inf')
    
    for volume in volumes:
        if volume > max_volume:
            max_volume = volume
        if volume < min_volume:
            min_volume = volume
    
    return max_volume, min_volume

if __name__ == '__main__':
    sample_volumes = [15.2, 30.8, 7.4, 60.1, 9.9]
    try:
        max_vol, min_vol = find_max_min_volumes(sample_volumes)
        print("Maximum Volume:", max_vol)
        print("Minimum Volume:", min_vol)
    except ValueError as e:
        print(e)