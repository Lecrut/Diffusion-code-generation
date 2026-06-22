def repeat_characters(input_string):
    result = ''.join(char * 2 for char in input_string)
    return result

if __name__ == '__main__':
    sample1 = "hello"
    result1 = repeat_characters(sample1)
    print(f"Input: {sample1}, Output: {result1}")

    sample2 = "abc"
    result2 = repeat_characters(sample2)
    print(f"Input: {sample2}, Output: {result2}")