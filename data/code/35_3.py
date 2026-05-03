if __name__ == '__main__':
    input_string = "Hello World"
    vowel_count = sum(1 for char in input_string if char.lower() in 'aeiou')
    print(vowel_count)