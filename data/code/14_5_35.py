def sort_volumes_descending(volumes):
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [1024, 512, 2048, 256, 768]
    sorted_volumes = sort_volumes_descending(sample_volumes)
    print(sorted_volumes)