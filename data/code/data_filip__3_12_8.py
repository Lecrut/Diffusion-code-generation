def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    translation_table = str.maketrans('', '', vowels)
    return s.translate(translation_table)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Python Programming"
    sample3 = "AEIOU aeiou"
    sample4 = "No vowels here bcdfg"
    print(remove_vowels(sample1))
    print(remove_vowels(sample2))
    print(remove_vowels(sample3))
    print(remove_vowels(sample4))