def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [34.5, 67.2, 12.8, 90.1, 45.3]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)