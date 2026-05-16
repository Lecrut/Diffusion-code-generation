def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        difference = volume1 - volume2
        print(f"{volume1} is greater than {volume2}. The difference is {difference}.")
    elif volume2 > volume1:
        difference = volume2 - volume1
        print(f"{volume2} is greater than {volume1}. The difference is {difference}.")
    else:
        print(f"{volume1} is equal to {volume2}.")
if __name__ == '__main__':
    v1 = 15.75
    v2 = 12.3
    compare_volumes(v1, v2)
    v3 = 45.0
    v4 = 45.0
    compare_volumes(v3, v4)
    v5 = 100.5
    v6 = 100.5
    compare_volumes(v5, v6)