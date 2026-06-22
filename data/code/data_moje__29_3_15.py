def count_vowels(strings):
    vowels = set('aeiouAEIOU')
    return sum(1 for s in strings for char in s if char in vowels)

if __name__ == '__main__':
    data = ["Hello", "World", "Python", "Programming"]
    result = count_vowels(data)
    print(result)