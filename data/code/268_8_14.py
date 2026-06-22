def get_first_word(line):
    return line.split()[0]

if __name__ == '__main__':
    sample_text = """Hello world
This is a test
Python programming"""
    lines = sample_text.strip().split('\n')
    first_words = [get_first_word(line) for line in lines]
    print(first_words)