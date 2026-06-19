def calculate_total_volume(file_content):
    total_volume = 0.0
    for line in file_content.splitlines():
        try:
            volume = float(line.strip())
            total_volume += volume
        except ValueError:
            print(f"Skipping invalid volume value: {line}")
    return total_volume

if __name__ == '__main__':
    sample_file_content = """12.5
30.75
invalid_value
45.0"""
    total_volume = calculate_total_volume(sample_file_content)
    print(total_volume)