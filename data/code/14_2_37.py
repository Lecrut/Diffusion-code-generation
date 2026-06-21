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
    sample_volumes = [15.2, 8.3, 47.6, 29.1, 0.9]
    max_vol, min_vol = find_max_min_volumes(sample_volumes)
    print(f"Max Volume: {max_vol}, Min Volume: {min_vol}")