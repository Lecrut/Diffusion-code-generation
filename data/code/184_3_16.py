def word_in_file(file_content, search_word):
    for line in file_content.split('\n'):
        if search_word in line:
            yield True
    yield False

if __name__ == '__main__':
    sample_file_content = "apple\nbanana\ncherry\ndate"
    search_for = "banana"
    result = any(word_in_file(sample_file_content, search_for))
    print(result)