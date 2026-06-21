COLOR_WORDS = ["red", "yellow", "purple", "orange"]

def initialize_word_dict(start, end):
    word_dict = {}
    for i in range(start, end + 1):
        if str(i) in COLOR_WORDS:
            word_dict[i] = str(i)
    return word_dict

if __name__ == '__main__':
    sample_dict = initialize_word_dict(1, 10)
    print(sample_dict)