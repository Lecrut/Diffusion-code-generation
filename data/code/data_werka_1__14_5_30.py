def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [234.5, 678.9, 123.4, 456.7, 890.1]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)