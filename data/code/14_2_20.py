def find_max_min_volumes(volumes):
    if not volumes:
        return None, None
    max_volume = max(volumes)
    min_volume = min(volumes)
    return max_volume, min_volume

if __name__ == '__main__':
    sample_volumes = [10.5, 23.4, 7.8, 45.6, 12.3]
    max_vol, min_vol = find_max_min_volumes(sample_volumes)
    print(max_vol, min_vol)