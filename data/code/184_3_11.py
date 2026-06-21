def word_in_file(file_content, target_word):
    for line in file_content.split('\n'):
        if target_word in line:
            yield True
            return
    yield False

if __name__ == '__main__':
    sample_file_content = "apple\nbanana\ncherry\ndate"
    target_word = "banana"
    result = next(word_in_file(sample_file_content, target_word))
    print(result)