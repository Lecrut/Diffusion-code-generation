def repeat_characters(input_string):
    return ''.join(char * 2 for char in input_string)

if __name__ == '__main__':
    sample1 = 'abc'
    result1 = repeat_characters(sample1)
    print(f"Input: {sample1}, Result: {result1}")
    
    sample2 = 'hello'
    result2 = repeat_characters(sample2)
    print(f"Input: {sample2}, Result: {result2}")