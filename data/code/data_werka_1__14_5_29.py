def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [10.5, 3.2, 7.8, 6.4, 9.1]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)