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
    sample_volumes = [10.5, 22.1, 5.0, 33.8, 15.7, 4.2, 28.9]
    max_v, min_v = find_min_max_volumes(sample_volumes)
    print(f"Maximum volume: {max_v}")
    print(f"Minimum volume: {min_v}")
    empty_list = []
    max_e, min_e = find_min_max_volumes(empty_list)
    print(f"Maximum volume in empty list: {max_e}")
    print(f"Minimum volume in empty list: {min_e}")