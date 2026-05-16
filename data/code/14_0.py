def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        difference = volume1 - volume2
        print(f"Volume 1 is greater than Volume 2 by {difference:.4f}")
    elif volume2 > volume1:
        difference = volume2 - volume1
        print(f"Volume 2 is greater than Volume 1 by {difference:.4f}")
    else:
        print("The volumes are equal.")
if __name__ == '__main__':
    v1 = 15.789
    v2 = 15.788
    compare_volumes(v1, v2)
    v3 = 100.5
    v4 = 100.5
    compare_volumes(v3, v4)
    v5 = 5.21
    v6 = 9.87
    compare_volumes(v5, v6)