def calculate_total_volume(file_content):
    total_volume = 0.0
    for line in file_content.splitlines():
        try:
            volume = float(line.strip())
            total_volume += volume
        except ValueError:
            print(f"Warning: Invalid volume value '{line}' ignored.")
    return total_volume

if __name__ == '__main__':
    sample_data = """12.5
34.75
invalid_value
89.0"""
    total = calculate_total_volume(sample_data)
    print(total)