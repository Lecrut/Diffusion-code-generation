def split_commas(s):
    result = []
    current = []
    for char in s:
        if char == ',':
            word = ''.join(current)
            if word:
                result.append(word)
            current = []
        else:
            current.append(char)
    word = ''.join(current)
    if word:
        result.append(word)
    return result

if __name__ == '__main__':
    print(split_commas("a,b,c"))
    print(split_commas("hello,,world"))
    print(split_commas("single"))
    print(split_commas(",,,,"))
    print(split_commas(""))
    print(split_commas("a,b,,c,d"))