def find_max_min_volumes(volumes):
    if not volumes:
        return None, None
    max_volume = min_volume = volumes[0]
    for volume in volumes[1:]:
        if volume > max_volume:
            max_volume = volume
        elif volume < min_volume:
            min_volume = volume
    return max_volume, min_volume

if __name__ == '__main__':
    sample_volumes = [3.5, 7.2, 1.8, 9.4, 5.6, 0.2, 10.1]
    max_vol, min_vol = find_max_min_volumes(sample_volumes)
    print(f"Maximum Volume: {max_vol}, Minimum Volume: {min_vol}")