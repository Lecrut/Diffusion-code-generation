def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [54.3, 78.2, 12.9, 67.5, 34.1]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)