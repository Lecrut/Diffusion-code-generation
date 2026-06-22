def compare_lengths(length1, length2):
    difference = abs(length1 - length2)
    if length1 > length2:
        return (difference, "First length is greater")
    elif length2 > length1:
        return (difference, "Second length is greater")
    else:
        return (difference, "Both lengths are equal")

if __name__ == '__main__':
    length1 = 7.5
    length2 = 9.3
    print(compare_lengths(length1, length2))