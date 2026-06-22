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
    samples = [
        "apple,banana,cherry",
        "one,,two",
        ",start,end,",
        "single",
        "",
        "a,b,c,d,e"
    ]
    for sample in samples:
        print(split_commas(sample))