def count_vowels(strings):
    vowels = set("aeiouAEIOU")
    return sum(1 for string in strings for char in string if char in vowels)

if __name__ == '__main__':
    sample_strings = ["Hello", "World", "Python", "List", "Comprehension"]
    result = count_vowels(sample_strings)
    print(result)