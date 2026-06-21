def get_nth_element(s, n):
    length = len(s)
    if n < 0:
        adjusted_index = length + n
    else:
        adjusted_index = n
    
    if adjusted_index < 0 or adjusted_index >= length:
        return None
    
    return s[adjusted_index]

if __name__ == '__main__':
    sample_string = 'hello'
    n = -1
    result = get_nth_element(sample_string, n)
    print(result)