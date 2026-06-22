def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [100.5, 234.7, 56.2, 89.0, 345.6]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)