import sys
def calculate_phrase_length(phrase):
    return len(phrase)
if __name__ == '__main__':
    sample_phrase_1 = "Hello World"
    sample_phrase_2 = "Python Optimization"
    sample_phrase_3 = ""
    sample_phrase_4 = "a"
    print(f"Length of '{sample_phrase_1}': {calculate_phrase_length(sample_phrase_1)}")
    print(f"Length of '{sample_phrase_2}': {calculate_phrase_length(sample_phrase_2)}")
    print(f"Length of '{sample_phrase_3}': {calculate_phrase_length(sample_phrase_3)}")
    print(f"Length of '{sample_phrase_4}': {calculate_phrase_length(sample_phrase_4)}")