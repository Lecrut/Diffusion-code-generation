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
                return f"{volume1} is larger than {volume2}"
            elif volume2 > volume1:
                return f"{volume2} is larger than {volume1}"
            else:
                return f"{volume1} is equal to {volume2}"
    except FileNotFoundError:
        return "Error: File not found."
    except ValueError:
        return "Error: Invalid data found in the file. Ensure all entries are valid numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    with open('volumes.txt', 'w') as f:
        f.write("100\n")
        f.write("150\n")
    result = compare_volumes('volumes.txt')
    print(result)