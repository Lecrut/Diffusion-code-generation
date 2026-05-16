def compare_temperatures(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                return None, None, None
            temp1_str = lines[0].strip()
            temp2_str = lines[1].strip()
            temp1 = float(temp1_str)
            temp2 = float(temp2_str)
            if temp1 is None or temp2 is None:
                return None, None, None
            difference = abs(temp1 - temp2)
            if difference > 5:
                status = "Discrepancy found"
            else:
                status = "Temperatures are within 5 degrees"
            return temp1, temp2, difference, status
    except FileNotFoundError:
        return None, None, None, "Error: File not found"
    except ValueError:
        return None, None, None, "Error: Invalid temperature format"
    except Exception as e:
        return None, None, None, f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_file_path = "temperatures.txt"
    with open(sample_file_path, 'w') as f:
        f.write("20.0\n")
        f.write("26.0\n")
    temp1, temp2, diff, status = compare_temperatures(sample_file_path)
    if temp1 is not None:
        print(f"Temperature 1: {temp1}°C")
        print(f"Temperature 2: {temp2}°C")
        print(f"Absolute Difference: {diff:.2f}°C")
        print(f"Status: {status}")