def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [34.5, 23.1, 45.6, 12.0, 78.9]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)