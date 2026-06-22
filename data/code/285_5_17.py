def check_adjacent_order(s):
    if not isinstance(s, str) or len(s) < 2:
        raise ValueError("Input must be a string of at least two characters.")
    
    result = []
    for i in range(len(s) - 1):
        if ord(s[i]) < ord(s[i + 1]):
            result.append('A')
        elif ord(s[i]) > ord(s[i + 1]):
            result.append('D')
        else:
            result.append('=')
    
    return result

if __name__ == '__main__':
    sample_string = "aBcDeFgHiJ"
    print(check_adjacent_order(sample_string))