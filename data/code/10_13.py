if __name__ == '__main__':
    temp1_str = "25.5"
    temp2_str = "30.1"
    try:
        temp1 = float(temp1_str)
        temp2 = float(temp2_str)
        if temp1 > temp2:
            print(f"Temperature 1 ({temp1}) is greater than Temperature 2 ({temp2}).")
        elif temp1 < temp2:
            print(f"Temperature 1 ({temp1}) is less than Temperature 2 ({temp2}).")
        else:
            print(f"Temperature 1 ({temp1}) is equal to Temperature 2 ({temp2}).")
    except ValueError:
        print("Error: One or both inputs are not valid numbers.")