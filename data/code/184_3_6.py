def stream_word_in_file(file_content, word):
    for line in file_content.split('\n'):
        if word in line:
            yield True
    yield False

if __name__ == '__main__':
    sample_file_content = "hello world\nthis is a test\nword search\nend of file"
    search_word = "test"
    result = next(stream_word_in_file(sample_file_content, search_word))
    print(result)