class WordChecker:
    WORD_TO_SEARCH = "world"

    @staticmethod
    def is_word_present(line):
        return WordChecker.WORD_TO_SEARCH in line

def stream_and_check(file_content):
    for line in file_content:
        if WordChecker.is_word_present(line):
            yield line.strip()

if __name__ == '__main__':
    sample_file = [
        "hello world\n",
        "python programming\n",
        "this is a test\n",
        "world\n"
    ]
    results = list(stream_and_check(sample_file))
    for result in results:
        print(result)