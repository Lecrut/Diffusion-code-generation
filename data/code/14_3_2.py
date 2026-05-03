def find_min_max_volumes(volumes):
    if not volumes:
        return None, None
    min_volume = volumes[0]
    max_volume = volumes[0]
    for volume in volumes[1:]:
        if volume < min_volume:
            min_volume = volume
        if volume > max_volume:
            max_volume = volume
    return max_volume, min_volume
if __name__ == '__main__':
    sample_volumes = [10.5, 22.1, 5.8, 30.9, 15.0, 8.2, 25.5]
    max_v, min_v = find_min_max_volumes(sample_volumes)
    print(f"Maximum volume: {max_v}")
    print(f"Minimum volume: {min_v}")
    sample_volumes_large = [1000, 50, 9999, 1, 50000, 12345]
    max_v_large, min_v_large = find_min_max_volumes(sample_volumes_large)
    print(f"Maximum volume (large set): {max_v_large}")
    print(f"Minimum volume (large set): {min_v_large}")
    empty_list = []
    max_v_empty, min_v_empty = find_min_max_volumes(empty_list)
    print(f"Result for empty list: Max={max_v_empty}, Min={min_v_empty}")