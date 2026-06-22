def compare_lengths(length1, length2):
    difference = abs(length1 - length2)
    if length1 > length2:
        result = "First length is greater"
    elif length2 > length1:
        result = "Second length is greater"
    else:
        result = "Both lengths are equal"
    return (difference, result)

if __name__ == '__main__':
    length1 = 5.75
    length2 = 3.25
    print(compare_lengths(length1, length2))