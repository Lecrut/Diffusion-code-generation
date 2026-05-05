import sys
line1 = "10 20 30 40"
line2 = "5 15 35 45"
if __name__ == '__main__':
    parts1 = line1.split()
    parts2 = line2.split()
    if len(parts1) > 2 and len(parts2) > 2:
        comparison1 = parts1[2]
        comparison2 = parts2[2]
        if comparison1 == comparison2:
            print("Equal")
        else:
            print("Not Equal")
    else:
        print("Insufficient data")