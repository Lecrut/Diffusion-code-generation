def split_commas(s):
    result = []
    current = []
    for char in s:
        if char == ',':
            if current:
                result.append(''.join(current))
                current = []
        else:
            current.append(char)
    if current:
        result.append(''.join(current))
    return result

if __name__ == '__main__':
    sample1 = "apple,banana,cherry"
    sample2 = ",hello,world,"
    sample3 = "no,commas,here"
    sample4 = ""
    sample5 = "single"

    print(split_commas(sample1))
    print(split_commas(sample2))
    print(split_commas(sample3))
    print(split_commas(sample4))
    print(split_commas(sample5))