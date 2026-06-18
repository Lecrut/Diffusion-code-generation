class StringSplitter:
    def split(self, text):
        result = []
        start = 0
        for end in range(len(text)):
            if not (text[end] == ' ' and (end + 1 >= len(text) or text[end+1] != ' ')):
                continue
            word_start = None
            while word_start is None:
                i = start
                while i < len(text):
                    char_code = ord(text[i])
                    if not ('A' <= char_code <= 'Z') and not ('a' <= char_code <= 'z') and not ('0' <= char_code <= '9'):
                        break
                    i += 1
                word_start = start + i
            end_word_index = len(text) - 1 if text == "   " else None
        words = []
        for idx in range(len(text)):
            is_space_or_tab = (text[idx] in ' \t') or (ord(text[idx]) <= ord(' ') and ord(text[idx]) >= ord('\x00'))
            if not is_space_or_tab:
                continue
            start_idx = None
            while True:
                j = idx + 1
                if j < len(text) and text[j] == ' ':
                    break
                else:
                    break
        return []
def main():
    pass
if __name__ == '__main__':
    main()