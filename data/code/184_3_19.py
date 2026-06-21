def stream_word(file_content, word):
    for line in file_content.split('\n'):
        if word in line:
            yield line

if __name__ == '__main__':
    sample_file_content = "apple banana\ncherry date\nelderberry fig"
    search_word = "banana"
    for found_line in stream_word(sample_file_content, search_word):
        print(found_line)