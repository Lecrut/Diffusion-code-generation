def sum_of_integers(int1=7, int2=8, int3=9, int4=10, int5=11, int6=12, int7=13):
    return sum([int1, int2, int3, int4, int5, int6, int7])

if __name__ == '__main__':
    print(f"Sum of (7, 8, 9, 10, 11, 12, 13): {sum_of_integers()}")