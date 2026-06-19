def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [10.5, 23.4, 7.8, 45.6, 12.3]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)