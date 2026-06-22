def combine_strings(str1, str2):
    return ''.join((str1, str2))

if __name__ == '__main__':
    sample_strings = {
        'greeting': ('Hello', 'World'),
        'language': ('Python', 'Programming')
    }
    
    for key, (str1, str2) in sample_strings.items():
        result = combine_strings(str1, str2)
        print(f"{key.capitalize()}: {result}")