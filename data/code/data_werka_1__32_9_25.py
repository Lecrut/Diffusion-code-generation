def calculate_phrase_length(phrase):
    return len(phrase)

if __name__ == '__main__':
    sample_values = ["Hello, World!", "Python", "", "OpenAI"]
    for value in sample_values:
        print(calculate_phrase_length(value))