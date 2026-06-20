import os

def calculate_total_volume_from_file(filepath: str) -> float:
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write("10.5\n")
            f.write("20.0\n")
            f.write("15.5\n")
    
    total_volume = 0.0
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                stripped = line.strip()
                if stripped:
                    try:
                        value = float(stripped)
                        if value >= 0:
                            total_volume += value
                        else:
                            raise ValueError("Negative volume not allowed")
                    except ValueError as e:
                        if "could not convert" in str(e) or "could not convert" in str(e):
                            continue
                        raise
    except IOError:
        raise

    return total_volume

if __name__ == '__main__':
    test_filepath = "sample_volumes.txt"
    result = calculate_total_volume_from_file(test_filepath)
    print(result)