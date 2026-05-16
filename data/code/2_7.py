def calculate_volumes(volumes):
    total_volume = sum(volumes)
    average_volume = total_volume / len(volumes)
    return total_volume, average_volume
if __name__ == '__main__':
    sample_volumes = [10.5, 22.0, 15.75, 30.25]
    total, average = calculate_volumes(sample_volumes)
    print(f"Sample Volumes: {sample_volumes}")
    print(f"Total Volume: {total}")
    print(f"Average Volume: {average}")