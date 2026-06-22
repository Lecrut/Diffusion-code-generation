import sys
import os

def convert_volumes(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied when accessing '{filename}'.")
        return []
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []

    results = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            volume = float(line)
            liters = volume
            cubic_meters = volume / 1000.0
            results.append((volume, liters, cubic_meters))
        except ValueError:
            print(f"Warning: Skipping invalid volume value '{line}'")
            continue

    for original, liters_val, cubic_meters_val in results:
        print(f"Original: {original} -> Liters: {liters_val} -> Cubic Meters: {cubic_meters_val}")
    return results

if __name__ == '__main__':
    sample_content = [
        "1000",
        "500",
        "1",
        "invalid",
        "2500"
    ]
    test_filename = "volumes.txt"
    
    with open(test_filename, "w") as f:
        for item in sample_content:
            f.write(item + "\n")
            
    convert_volumes(test_filename)
    
    os.remove(test_filename)