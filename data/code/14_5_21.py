def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [34.5, 21.7, 56.9, 10.2, 88.3]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)