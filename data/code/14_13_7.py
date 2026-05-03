def compare_volumes(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                return "Error: Not enough volume measurements found."
            volume1 = float(lines[0].strip())
            volume2 = float(lines[1].strip())
            if volume1 > volume2:
                return f"Volume 1 ({volume1}) is larger than Volume 2 ({volume2})."
            elif volume2 > volume1:
                return f"Volume 2 ({volume2}) is larger than Volume 1 ({volume1})."
            else:
                return f"Volume 1 ({volume1}) and Volume 2 ({volume2}) are equal."
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except ValueError:
        return f"Error: Could not convert one or more lines in '{filename}' to a valid number."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    filename = 'volumes.txt'
    try:
        with open(filename, 'w') as f:
            f.write("100\n")
            f.write("150\n")
            f.write("200\n")
        result = compare_volumes(filename)
        print(result)
    except IOError as e:
        print(f"File I/O error during setup: {e}")