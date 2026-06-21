def stream_word(file_content, target_word):
    for line in file_content.split('\n'):
        if target_word in line:
            yield line

if __name__ == '__main__':
    sample_file_content = """This is a sample line with the word example.
Another line without the target word.
Yet another line containing the word example."""
    target_word = 'example'
    
    for line in stream_word(sample_file_content, target_word):
        print(line)