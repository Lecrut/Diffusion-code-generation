def process_volume_file(file_path):
    liters_to_cubic_meters = 0.001
    results = []
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return ["Error: File not found"]
    except IOError:
        return ["Error: Could not read file"]

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if not parts:
            continue
        value_str = parts[0]
        try:
            value = float(value_str)
        except ValueError:
            results.append(f"Error: Invalid number '{value_str}'")
            continue
        liters = value
        cubic_meters = liters * liters_to_cubic_meters
        results.append((liters, cubic_meters))
    return results

if __name__ == '__main__':
    import os
    import tempfile

    temp_path = None
    try:
        fd, temp_path = tempfile.mkstemp(suffix='.txt')
        sample_data = b"1.0\n2.5\n10\nabc\n-5.0\n"
        with os.fdopen(fd, 'wb') as f:
            f.write(sample_data)

        results = process_volume_file(temp_path)
        for item in results:
            if isinstance(item, tuple):
                liters, cubic_meters = item
                print(f"{liters} liters = {cubic_meters} cubic meters")
            else:
                print(item)
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)