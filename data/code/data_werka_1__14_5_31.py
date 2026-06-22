def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [120.5, 45.2, 300.8, 67.4, 90.1]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)