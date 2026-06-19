def find_max_min_volumes(volumes):
    if not volumes:
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
    sample_volumes = [10.5, 23.7, 4.8, 99.1, 0.0, -5.6]
    max_vol, min_vol = find_max_min_volumes(sample_volumes)
    print("Max Volume:", max_vol)
    print("Min Volume:", min_vol)