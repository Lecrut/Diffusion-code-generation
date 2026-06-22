def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [10.5, 23.4, 7.8, 56.9, 34.2]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)