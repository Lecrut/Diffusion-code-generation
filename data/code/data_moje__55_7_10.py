import string

def reverse_alphabet_triangle(start_char, end_char):
    alphabet = string.ascii_lowercase
    reversed_alphabet = list(reversed(alphabet))
    start_index = reversed_alphabet.index(start_char.lower())
    end_index = reversed_alphabet.index(end_char.lower())
    
    if start_index < end_index:
        segment = reversed_alphabet[start_index:end_index + 1]
    else:
        segment = reversed_alphabet[end_index:start_index + 1]
        segment.reverse()
    
    result = []
    width = len(segment)
    
    for i, char in enumerate(segment):
        line = ' ' * (width - i - 1) + ' '.join([char] * (i + 1))
        result.append(line)
        
    for i in range(len(segment) - 2, -1, -1):
        line = ' ' * (width - i - 1) + ' '.join([segment[i]] * (i + 1))
        result.append(line)
        
    return '\n'.join(result)

if __name__ == '__main__':
    start = 'a'
    end = 'd'
    print(reverse_alphabet_triangle(start, end))