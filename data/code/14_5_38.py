def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [150, 300, 75, 200, 450]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)