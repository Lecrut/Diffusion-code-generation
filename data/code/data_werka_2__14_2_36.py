def find_max_min_volumes(volumes):
    if not volumes:
        raise ValueError("The volume list cannot be empty")
    
    max_volume = float('-inf')
    min_volume = float('inf')
    
    for volume in volumes:
        if volume > max_volume:
            max_volume = volume
        if volume < min_volume:
            min_volume = volume
    
    return max_volume, min_volume

if __name__ == '__main__':
    sample_volumes = [10.5, 23.4, 7.8, 45.6, 12.3]
    max_vol, min_vol = find_max_min_volumes(sample_volumes)
    print("Maximum Volume:", max_vol)
    print("Minimum Volume:", min_vol)