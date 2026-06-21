def word_in_file(file_content, target_word):
    for line in file_content.split('\n'):
        if target_word in line:
            yield True
            return
    yield False

if __name__ == '__main__':
    sample_content = "This is a test.\nAnother line with the word.\nEnd of content."
    target = "word"
    result = next(word_in_file(sample_content, target))
    print(result)