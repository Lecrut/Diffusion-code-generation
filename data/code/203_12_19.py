def compare_strings(s1, s2):
    len_diff = len(s1) - len(s2)
    is_longer = len(s1) > len(s2)
    
    if not is_longer and not (s1 < s2):
        return (0, False)
    elif is_longer or (len_diff == 0 and s1 < s2):
        return (abs(len_diff), True)
    else:
        return (abs(len_diff), False)

if __name__ == '__main__':
    result1 = compare_strings("apple", "banana")
    print(f"Comparing 'apple' and 'banana': {result1}")
    
    result2 = compare_strings("dog", "cat")
    print(f"Comparing 'dog' and 'cat': {result2}")
    
    result3 = compare_strings("hello", "hello")
    print(f"Comparing 'hello' and 'hello': {result3}")