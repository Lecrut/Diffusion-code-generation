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
    sample_input = "apple,banana,,cherry,,,"
    output = split_commas(sample_input)
    print(output)