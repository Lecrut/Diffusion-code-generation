def count_uppercase_letters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World!"
    print(count_uppercase_letters(sample_string))