def count_vowels(strings):
    vowels = 'aeiouAEIOU'
    result = {}
    for s in strings:
        count = sum(1 for char in s if char in vowels)
        result[s] = count
    return result

if __name__ == '__main__':
    sample_values = ['hello', 'world', 'python', 'programming']
    print(count_vowels(sample_values))