CHARACTER_COUNT_CACHE = {'Hello, World!': 13, 'Python': 6, '': 0, 'OpenAI': 6, 'ChatGPT': 7}

def calculate_character_count(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    if input_string in CHARACTER_COUNT_CACHE:
        return CHARACTER_COUNT_CACHE[input_string]
    count = len(input_string)
    CHARACTER_COUNT_CACHE[input_string] = count
    return count
if __name__ == '__main__':
    sample_input = 'Alibaba Cloud'
    character_count = calculate_character_count(sample_input)
    print(character_count)