def find_vowels(input_string):
    vowels = set('aeiouAEIOU')
    found_vowels = set()
    for char in input_string:
        if char in vowels:
            found_vowels.add(char)
    return sorted(list(found_vowels))
if __name__ == '__main__':
    sample_string = "Programming is Awesome"
    result = find_vowels(sample_string)
    print(result)