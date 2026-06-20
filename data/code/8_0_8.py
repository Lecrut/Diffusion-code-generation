def split_commas(s):
    if not s:
        return []
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
    print(split_commas("hello,,world"))
    print(split_commas("single"))
    print(split_commas(","))
    print(split_commas(""))
    print(split_commas("a,b,c,d,e"))