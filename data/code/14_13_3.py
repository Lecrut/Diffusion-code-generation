def compare_volumes(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                return "Error: Not enough volume measurements found."
            volume1_str = lines[0].strip()
            volume2_str = lines[1].strip()
            if not volume1_str or not volume2_str:
                return "Error: One or both volume measurements are empty."
            volume1 = float(volume1_str)
            volume2 = float(volume2_str)
            if volume1 > volume2:
                return f"Volume 1 ({volume1}) is larger than Volume 2 ({volume2})."
            elif volume2 > volume1:
                return f"Volume 2 ({volume2}) is larger than Volume 1 ({volume1})."
            else:
                return f"Volume 1 ({volume1}) and Volume 2 ({volume2}) are equal."
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except ValueError:
        return f"Error: Could not convert one or both measurements to a number in '{filename}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    filename = 'volumes.txt'
    with open(filename, 'w') as f:
        f.write("100\n")
        f.write("250\n")
    result = compare_volumes(filename)
    print(result)