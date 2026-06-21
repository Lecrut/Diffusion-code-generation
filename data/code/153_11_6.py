def substring_exists(data, substring):
    return substring in data

if __name__ == '__main__':
    strings = ['apple', 'banana', 'cherry']
    sub1 = 'an'
    result1 = substring_exists(strings, sub1)
    print(f"Strings: {strings}, Substring: {sub1}, Exists: {result1}")

    strings2 = ['hello', 'world', 'python']
    sub2 = 'java'
    result2 = substring_exists(strings2, sub2)
    print(f"Strings: {strings2}, Substring: {sub2}, Exists: {result2}")