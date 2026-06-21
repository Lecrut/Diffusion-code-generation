from collections import Counter

def char_frequency_difference(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    
    difference = {char: counter1[char] - counter2[char] for char in set(counter1) | set(counter2)}
    return {char: abs(diff) for char, diff in difference.items() if diff != 0}

if __name__ == '__main__':
    result = char_frequency_difference('hello', 'world')
    print(result)