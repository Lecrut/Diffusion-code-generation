def combine_strings(str1, str2):
    return ''.join([str1, str2])

if __name__ == '__main__':
    sample_values = {
        'greeting': ('Hello', 'World'),
        'language': ('Python', 'Programming')
    }
    
    for key, (string_a, string_b) in sample_values.items():
        result = combine_strings(string_a, string_b)
        print(f"{key.capitalize()} combined: {result}")