import sys
if __name__ == '__main__':
    line1 = "10 20"
    line2 = "5 15"
    parts1 = line1.split()
    parts2 = line2.split()
    sum1 = sum(int(x) for x in parts1)
    sum2 = sum(int(x) for x in parts2)
    if sum1 > sum2:
        print(f"Sum of the first set ({sum1}) is larger than the sum of the second set ({sum2}).")
    elif sum2 > sum1:
        print(f"Sum of the second set ({sum2}) is larger than the sum of the first set ({sum1}).")
    else:
        print(f"The sums are equal: {sum1}.")