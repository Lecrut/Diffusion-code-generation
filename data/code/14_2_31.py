def find_max_min_volumes(volumes):
    if not volumes:
        return None, None
    max_volume = min_volume = volumes[0]
    for volume in volumes:
        if volume > max_volume:
            max_volume = volume
        elif volume < min_volume:
            min_volume = volume
    return max_volume, min_volume

if __name__ == '__main__':
    sample_volumes = [15.2, 3.8, 7.4, 9.1, 2.6, 11.0, 15.2]
    max_vol, min_vol = find_max_min_volumes(sample_volumes)
    print("Maximum Volume:", max_vol)
    print("Minimum Volume:", min_vol)