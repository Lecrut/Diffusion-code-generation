def count_consonants(s):
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = 0
    for char in s:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! 1234"
    result = count_consonants(sample_string)
    print(result)