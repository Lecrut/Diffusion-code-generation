def compare_lengths(a, b):
    if a > b:
        return "greater"
    elif a < b:
        return "less"
    else:
        return "equal"
if __name__ == '__main__':
    val1 = 10.5
    val2 = 10.5
    print(f"Comparing {val1} and {val2}: {compare_lengths(val1, val2)}")
    val3 = 5.2
    val4 = 8.9
    print(f"Comparing {val3} and {val4}: {compare_lengths(val3, val4)}")
    val5 = 20.0
    val6 = 15.75
    print(f"Comparing {val5} and {val6}: {compare_lengths(val5, val6)}")