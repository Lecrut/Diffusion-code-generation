def stream_word(file_content, target_word):
    for line in file_content.split('\n'):
        if target_word in line:
            yield line

if __name__ == '__main__':
    sample_file_content = "apple\nbanana\ncherry\ndate\nelderberry"
    target_word = "banana"
    found_lines = list(stream_word(sample_file_content, target_word))
    print(found_lines)