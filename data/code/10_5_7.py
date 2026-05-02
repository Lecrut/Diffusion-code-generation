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
            difference = abs(temp1 - temp2)
            if difference > 5:
                discrepancy_flag = True
            else:
                discrepancy_flag = False
            return temp1, temp2, discrepancy_flag
    except FileNotFoundError:
        return None, None, None
    except ValueError:
        return None, None, None
if __name__ == '__main__':
    file_name = "temperatures.txt"
    with open(file_name, 'w') as f:
        f.write("20.0\n")
        f.write("28.0\n")
    temp1, temp2, flag = compare_temperatures(file_name)
    if temp1 is not None:
        print(f"Temperature 1: {temp1}°C")
        print(f"Temperature 2: {temp2}°C")
        if flag:
            print("Discrepancy detected: Greater than 5°C")
        else:
            print("Temperatures are within 5°C of each other")