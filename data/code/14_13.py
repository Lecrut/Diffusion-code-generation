def compare_volumes(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                return None, None
            volume1_str = lines[0].strip()
            volume2_str = lines[1].strip()
            if not volume1_str.isdigit() or not volume2_str.isdigit():
                return None, None
            volume1 = float(volume1_str)
            volume2 = float(volume2_str)
            if volume1 > volume2:
                return volume1, volume2
            elif volume2 > volume1:
                return volume2, volume1
            else:
                return volume1, volume2
    except FileNotFoundError:
        return None, None
    except IOError:
        return None, None
    except Exception:
        return None, None
if __name__ == '__main__':
    filename = 'volumes.txt'
    with open(filename, 'w') as f:
        f.write("100\n")
        f.write("250\n")
    v1, v2 = compare_volumes(filename)
    if v1 is not None:
        print(f"Volume 1: {v1}")
        print(f"Volume 2: {v2}")
        if v1 > v2:
            print("Volume 1 is larger.")
        elif v2 > v1:
            print("Volume 2 is larger.")
        else:
            print("Volumes are equal.")
    else:
        print("Error: Could not read or compare volumes.")