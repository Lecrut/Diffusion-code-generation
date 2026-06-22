def convert_to_title_case(strings):
    def to_title(s):
        return s.title()
    
    title_cased_list = [to_title(s) for s in strings]
    return title_cased_list

if __name__ == '__main__':
    sample_strings = ["the quick brown fox", "jumps OVER the lazy dog", "data SCIENCE and AI"]
    title_cased_strings = convert_to_title_case(sample_strings)
    print(title_cased_strings)