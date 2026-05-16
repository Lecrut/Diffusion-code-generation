def sort_volumes_descending(volumes):
    volumes.sort(reverse=True)
    return volumes
if __name__ == '__main__':
    sample_volumes = [10.5, 5.2, 22.8, 1.1, 15.0]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)