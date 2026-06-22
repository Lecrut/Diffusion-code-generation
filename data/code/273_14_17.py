def repeat_characters(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    result = ''.join(char * 2 for char in input_string)
    return result

if __name__ == '__main__':
    sample1 = "abc"
    print(f"Input: {sample1}, Output: {repeat_characters(sample1)}")
    
    sample2 = "hello"
    print(f"Input: {sample2}, Output: {repeat_characters(sample2)}")
    
    sample3 = ""
    print(f"Input: {sample3}, Output: {repeat_characters(sample3)}")