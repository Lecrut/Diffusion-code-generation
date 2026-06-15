import sys
def get_initial_word(input_string):
    return input_string.split()[0]
sample_input = "This is a sample sentence"
result = get_initial_word(sample_input)
print(result)
if __name__ == '__main__':
    pass