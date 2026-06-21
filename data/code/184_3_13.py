def stream_word(file_content, target_word):
    for line in file_content.split('\n'):
        if target_word in line:
            yield True
            return

if __name__ == '__main__':
    sample_file_content = "apple\nbanana\ncherry\ndate"
    target_word = "banana"
    result = next(stream_word(sample_file_content, target_word))
    print(result)