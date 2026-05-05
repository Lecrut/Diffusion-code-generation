import sys
line1 = "10 20 30 40"
line2 = "5 15 30 50"
if __name__ == '__main__':
    parts1 = line1.split()
    parts2 = line2.split()
    if len(parts1) > 2 and len(parts2) > 2:
        comparison_value1 = parts1[2]
        comparison_value2 = parts2[2]
        if comparison_value1 == comparison_value2:
            print("Equal")
        else:
            print("Not Equal")
    else:
        print("Insufficient data")