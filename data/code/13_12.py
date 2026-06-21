def get_nth_element(s, n):
    length = len(s)
    if n < 0:
        index = n + length
        if index < 0:
            index = 0
        elif index >= length:
            return None
    else:
        if n >= length:
            return None
        index = n
    return s[index]

if __name__ == '__main__':
    text = "Hello, World!"
    positive_result = get_nth_element(text, 0)
    negative_result = get_nth_element(text, -1)
    out_of_bounds_negative_result = get_nth_element(text, -100)
    out_of_bounds_positive_result = get_nth_element(text, 100)
    
    print(positive_result)
    print(negative_result)
    print(out_of_bounds_negative_result)
    print(out_of_bounds_positive_result)