def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [3.5, 1.2, 7.8, 4.6, 2.9]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)