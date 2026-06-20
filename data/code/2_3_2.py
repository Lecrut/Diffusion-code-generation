def calculate_total_volume(volumes):
    return sum(volumes.values())

if __name__ == '__main__':
    sample_data = {"cube": 10, "sphere": 15, "cylinder": 5}
    total = calculate_total_volume(sample_data)
    print(total)