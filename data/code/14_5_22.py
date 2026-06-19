def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [100, 234, 567, 89, 345, 123]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)