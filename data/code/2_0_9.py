import os
import tempfile

def calculate_total_volume(file_path: str) -> float:
    total_volume = 0.0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    value = float(stripped)
                    if value >= 0:
                        total_volume += value
                except ValueError:
                    continue
    except FileNotFoundError:
        return 0.0
    except IOError:
        return 0.0
    return total_volume

def main():
    sample_values = ["10.5", "20.0", "30.5", "\n", "invalid"]
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
        tmp_file.write('\n'.join(sample_values))
        tmp_path = tmp_file.name
    
    try:
        result = calculate_total_volume(tmp_path)
        print(result)
    finally:
        os.unlink(tmp_path)

if __name__ == '__main__':
    main()