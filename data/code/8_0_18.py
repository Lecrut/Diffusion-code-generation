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
    print(split_commas("a,b,c"))
    print(split_commas("hello"))
    print(split_commas(",,"))
    print(split_commas("a,,b"))
    print(split_commas(""))