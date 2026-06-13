class TextAnalyzer:
    def scan_document(self, filepath, target_word):
        found_lines = []
        try:
            with open(filepath, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    if target_word in line:
                        found_lines.append(line_num)
        except FileNotFoundError:
            return []
        return found_lines
if __name__ == '__main__':
    sample_file_path = "sample.txt"
    with open(sample_file_path, 'w') as f:
        f.write("This is line one.\n")
        f.write("The quick brown fox jumps over the lazy dog.\n")
        f.write("Fox is a cunning animal.\n")
        f.write("Another line with the fox.\n")
    analyzer = TextAnalyzer()
    target = "fox"
    result = analyzer.scan_document(sample_file_path, target)
    print(result)