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
    sample_filename = "sample.txt"
    with open(sample_filename, 'w') as f:
        f.write("This is the first line.\n")
        f.write("The quick brown fox jumps over the lazy dog.\n")
        f.write("Foxes are clever animals.\n")
        f.write("Another line with the target word.\n")
    analyzer = TextAnalyzer()
    target = "fox"
    file_path = sample_filename
    results = analyzer.scan_document(file_path, target)
    print(f"Lines containing '{target}': {results}")