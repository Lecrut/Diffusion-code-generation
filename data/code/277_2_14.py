vowels_map = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
              'A': True, 'E': True, 'I': True, 'O': True, 'U': True}

def count_vowels(s):
    count = 0
    for char in s:
        if vowels_map.get(char):
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Programming is fun!"
    print(count_vowels(sample_string))