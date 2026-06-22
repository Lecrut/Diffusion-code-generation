def calculate_total_volume(file_content):
    total_volume = 0.0
    for line in file_content.splitlines():
        try:
            volume = float(line.strip())
            total_volume += volume
        except ValueError:
            print(f"Warning: Non-numeric value encountered and ignored - {line}")
    return total_volume

if __name__ == '__main__':
    sample_file_content = """10.5
20.3
abc
30.7"""
    total_volume = calculate_total_volume(sample_file_content)
    print(total_volume)