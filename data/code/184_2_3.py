import os
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
    sample_filename = "sample_document.txt"
    sample_content = [
        "This is the first line.",
        "The quick brown fox jumps over the lazy dog.",
        "Another line with the target word.",
        "This line has no match.",
        "The end of the document."
    ]
    with open(sample_filename, 'w') as f:
        for line in sample_content:
            f.write(line + "\n")
    analyzer = TextAnalyzer()
    target = "word"
    file_path = sample_filename
    results = analyzer.scan_document(file_path, target)
    print(f"Searching for '{target}' in {sample_filename}:")
    if results:
        for line in results:
            print(f"Found at line: {line}")
    else:
        print(f"'{target}' not found.")