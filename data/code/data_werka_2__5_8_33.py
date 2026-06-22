def compare_lengths(length1, length2):
    difference = abs(length1 - length2)
    if length1 > length2:
        description = "First length is greater"
    elif length2 > length1:
        description = "Second length is greater"
    else:
        description = "Both lengths are equal"
    return (difference, description)

if __name__ == '__main__':
    first_length = 7.5
    second_length = 4.3
    result = compare_lengths(first_length, second_length)
    print(result)