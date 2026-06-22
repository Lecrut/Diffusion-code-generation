def calculate_total_volume(file_path):
    total_volume = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                volume = float(line)
                total_volume += volume
            except ValueError:
                continue
    return total_volume

if __name__ == '__main__':
    import tempfile
    import os
    
    sample_data = "10.5\n20.3\n30.1\ninvalid\n40.0\n"
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        tmp.write(sample_data)
        tmp_path = tmp.name
    
    try:
        result = calculate_total_volume(tmp_path)
        print(result)
    finally:
        os.unlink(tmp_path)