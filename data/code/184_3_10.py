def stream_word(file_content, target_word):
    for line in file_content.split('\n'):
        if target_word in line:
            yield line

if __name__ == '__main__':
    sample_file_content = "apple banana\ncherry date\nelderberry fig"
    target_word = "banana"
    for matching_line in stream_word(sample_file_content, target_word):
        print(matching_line)