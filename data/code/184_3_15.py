def word_line_stream(file_content, target_word):
    for line in file_content.split('\n'):
        if target_word in line:
            yield True
        else:
            yield False

if __name__ == '__main__':
    sample_content = "hello world\npython programming\ntest this is a test\nworld"
    target = "world"
    streamer = word_line_stream(sample_content, target)
    for result in streamer:
        print(result)