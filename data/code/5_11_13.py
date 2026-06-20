def process_strings(input_tuple):
    result = []
    for s in input_tuple:
        if len(s) == 0:
            result.append(s)
        else:
            result.append(s[0].upper() + s[1:].lower())
    return tuple(result)

if __name__ == '__main__':
    sample_data = ("hELLO", "wORLD", "PyThOn", "", "cASE")
    output = process_strings(sample_data)
    print(output)