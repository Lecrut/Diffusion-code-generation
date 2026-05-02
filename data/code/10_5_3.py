def compare_temperatures(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                return None
            temp1 = float(lines[0].strip())
            temp2 = float(lines[1].strip())
            if abs(temp1 - temp2) > 5:
                return f"Discrepancy found: {abs(temp1 - temp2):.2f}°C"
            else:
                return "Temperatures are within 5°C of each other."
    except FileNotFoundError:
        return "Error: File not found."
    except ValueError:
        return "Error: Could not read valid temperature values."
if __name__ == '__main__':
    file_name = "temperatures.txt"
    with open(file_name, 'w') as f:
        f.write("20.0\n")
        f.write("26.0\n")
    result = compare_temperatures(file_name)
    print(result)