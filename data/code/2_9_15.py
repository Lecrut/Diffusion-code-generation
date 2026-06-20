def calculate_total_volume(file_path):
    total = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                value = float(line)
                total += value
            except ValueError:
                continue
    return total

if __name__ == '__main__':
    sample_data = "10.5\n20.0\nabc\n30.5\n"
    
    import tempfile
    import os
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        tmp.write(sample_data)
        tmp_path = tmp.name
    
    try:
        result = calculate_total_volume(tmp_path)
        print(result)
    finally:
        os.unlink(tmp_path)