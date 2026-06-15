import sys
def sort_and_join_words(input_string):
    words = input_string.split()
    words.sort()
    return " ".join(words)
if __name__ == '__main__':
    sample_input = "hello world python sorting algorithm"
    result = sort_and_join_words(sample_input)
    print(result)