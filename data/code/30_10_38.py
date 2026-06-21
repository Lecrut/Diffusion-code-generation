def swap_adjacent_characters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    result = []
    for i in range(0, len(s) - 1, 2):
        result.append(s[i + 1])
        result.append(s[i])
    
    if len(s) % 2 != 0:
        result.append(s[-1])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_string = 'abcdefg'
    try:
        result = swap_adjacent_characters(sample_string)
        print(result)
    except ValueError as e:
        print(e)