def count_uppercase_letters(input_string):
    count = 0
    for char in input_string:
        if char.isupper():
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World!"
    print(count_uppercase_letters(sample_string))