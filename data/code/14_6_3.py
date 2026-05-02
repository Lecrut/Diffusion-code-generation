import sys
def compare_volumes(vol1_str, vol2_str):
    try:
        vol1 = float(vol1_str)
        vol2 = float(vol2_str)
        if vol1 > vol2:
            print("Volume 1 is greater than Volume 2")
        elif vol1 < vol2:
            print("Volume 1 is less than Volume 2")
        else:
            print("Volumes are equal")
    except ValueError:
        print("Error: One or both inputs are not valid numbers")
if __name__ == '__main__':
    volume1_input = "150.5"
    volume2_input = "150.5"
    compare_volumes(volume1_input, volume2_input)