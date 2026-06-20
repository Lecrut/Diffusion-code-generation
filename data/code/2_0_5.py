import os
import tempfile

def calculate_total_volume(file_path):
    total_volume = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            try:
                volume = float(stripped)
                total_volume += volume
            except ValueError:
                raise ValueError(f"Invalid volume measurement in file: {stripped}")
    return total_volume

def main():
    sample_data = "10.5\n20.3\n15.2\ninvalid\n"
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        tmp.write(sample_data)
        tmp_path = tmp.name

    try:
        total = calculate_total_volume(tmp_path)
        print(total)
    except ValueError:
        print(0)
    finally:
        os.unlink(tmp_path)

if __name__ == '__main__':
    main()