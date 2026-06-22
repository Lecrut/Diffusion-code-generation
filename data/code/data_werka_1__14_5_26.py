def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [100, 234, 56, 78, 90, 345, 67]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)