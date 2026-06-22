def split_commas(s):
    result = []
    current = []
    for char in s:
        if char == ',':
            token = ''.join(current)
            if token:
                result.append(token)
            current = []
        else:
            current.append(char)
    token = ''.join(current)
    if token:
        result.append(token)
    return result

if __name__ == '__main__':
    sample_inputs = [
        "a,b,c",
        ",,,",
        "single",
        "one,,two",
        "",
        "  spaces  ,  more  "
    ]
    for sample in sample_inputs:
        print(split_commas(sample))