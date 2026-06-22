def count_uppercase_letters(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Python Programming"
    uppercase_count = count_uppercase_letters(sample_string)
    print(uppercase_count)