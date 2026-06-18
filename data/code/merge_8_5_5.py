import sys
if __name__ == '__main__':
    line1 = "10 20"
    line2 = "5 15"
    parts1 = line1.split()
    parts2 = line2.split()
    sum1 = sum(int(x) for x in parts1)
    sum2 = sum(int(x) for x in parts2)
    if sum1 > sum2:
        print(f"Sum from first line ({line1}): {sum1} is larger than sum from second line ({line2}): {sum2}")
    elif sum2 > sum1:
        print(f"Sum from first line ({line1}): {sum1} is smaller than sum from second line ({line2}): {sum2}")
    else:
        print(f"The sums are equal. Sum from first line ({line1}): {sum1}, Sum from second line ({line2}): {sum2}")