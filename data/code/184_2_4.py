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
    class MockFileHandler:
        def __init__(self):
            self.content = ["This is line one.", "The quick brown fox.", "Fox jumps over the lazy dog.", "Another line with the fox."]
        def read(self, mode):
            if mode == 'r':
                return self.content
            return None
    class MockFile:
        def __init__(self, content):
            self._content = content
        def read(self):
            return self._content
    import io
    import os
    file_content = io.StringIO('\n'.join(["This is line one.", "The quick brown fox.", "Fox jumps over the lazy dog.", "Another line with the fox."]))
    filepath = "sample.txt"
    with open(filepath, 'w') as f:
        f.write('\n'.join(["This is line one.", "The quick brown fox.", "Fox jumps over the lazy dog.", "Another line with the fox."]))
    analyzer = TextAnalyzer()
    target = "fox"
    results = analyzer.scan_document(filepath, target)
    print(results)