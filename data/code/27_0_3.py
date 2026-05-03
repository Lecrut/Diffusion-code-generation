def check_difference(a, b):
    return a != b
if __name__ == '__main__':
    val1 = 10
    val2 = 10
    val3 = 5
    val4 = 8.5
    print(f"10 and 10 are different: {check_difference(val1, val2)}")
    print(f"10 and 5 are different: {check_difference(val1, val3)}")
    print(f"8.5 and 10 are different: {check_difference(val4, val1)}")
    print(f"5 and 8.5 are different: {check_difference(val3, val4)}")