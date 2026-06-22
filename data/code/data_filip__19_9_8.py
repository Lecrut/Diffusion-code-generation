class EscapableRLE:
    ESCAPE_CHAR = '\\'
    ESCAPE_COUNT = 'c'
    ESCAPE_LITERAL = 'l'
    SPECIAL_SYMBOLS = ['.', '?', '!']

    @staticmethod
    def _is_special_char(char):
        return char in EscapableRLE.SPECIAL_SYMBOLS

    @staticmethod
    def _is_escape_count(char):
        return char == EscapableRLE.ESCAPE_COUNT

    @staticmethod
    def _is_escape_literal(char):
        return char == EscapableRLE.ESCAPE_LITERAL

    @staticmethod
    def _is_escape_char(char):
        return char == EscapableRLE.ESCAPE_CHAR

    @classmethod
    def encode(cls, text: str) -> str:
        if not text:
            return ''
        result = []
        i = 0
        length = len(text)
        while i < length:
            char = text[i]
            count = 1
            while i + count < length and text[i + count] == char and (not cls._is_special_char(char)):
                count += 1
            if count > 1:
                result.append(str(count))
                result.append(char)
                i += count
            else:
                if cls._is_special_char(char):
                    result.append(cls.ESCAPE_CHAR)
                    result.append(cls.ESCAPE_LITERAL)
                    result.append(char)
                elif cls._is_escape_char(char):
                    result.append(cls.ESCAPE_CHAR)
                    result.append(cls.ESCAPE_CHAR)
                else:
                    result.append(char)
                i += 1
        return ''.join(result)

    @classmethod
    def decode(cls, compressed: str) -> str:
        if not compressed:
            return ''
        result = []
        i = 0
        length = len(compressed)
        while i < length:
            char = compressed[i]
            if cls._is_escape_char(char):
                if i + 1 < length:
                    next_char = compressed[i + 1]
                    if cls._is_escape_literal(next_char):
                        if i + 2 < length:
                            literal_char = compressed[i + 2]
                            result.append(literal_char)
                            i += 3
                            continue
                        else:
                            result.append(char)
                            i += 1
                    elif cls._is_escape_count(next_char):
                        result.append(char)
                        i += 1
                    else:
                        result.append(char)
                        i += 1
                else:
                    result.append(char)
                    i += 1
            else:
                count_str = ''
                while i < length and compressed[i].isdigit():
                    count_str += compressed[i]
                    i += 1
                if count_str:
                    if i < length:
                        count = int(count_str)
                        repeat_char = compressed[i]
                        if cls._is_escape_char(repeat_char) and i + 1 < length:
                            next_char = compressed[i + 1]
                            if cls._is_escape_literal(next_char):
                                if i + 2 < length:
                                    literal_char = compressed[i + 2]
                                    result.append(literal_char * count)
                                    i += 3
                                else:
                                    result.append(repeat_char * count)
                                    i += 1
                            elif cls._is_escape_count(next_char):
                                result.append(repeat_char * count)
                                i += 1
                            else:
                                result.append(repeat_char * count)
                                i += 1
                        else:
                            result.append(repeat_char * count)
                            i += 1
                    else:
                        result.append(count_str)
                else:
                    result.append(char)
                    i += 1
        return ''.join(result)
if __name__ == '__main__':
    rle = EscapableRLE()
    text1 = 'aaabbccc'
    encoded1 = rle.encode(text1)
    decoded1 = rle.decode(encoded1)
    text2 = '!Hello'
    encoded2 = rle.encode(text2)
    decoded2 = rle.decode(encoded2)
    text3 = '555'
    encoded3 = rle.encode(text3)
    decoded3 = rle.decode(encoded3)
    text4 = 'Aa'
    encoded4 = rle.encode(text4)
    decoded4 = rle.decode(encoded4)
    print(f"Encode '{text1}': {encoded1}")
    print(f"Decode '{encoded1}': {decoded1}")
    print(f"Encode '{text2}': {encoded2}")
    print(f"Decode '{encoded2}': {decoded2}")
    print(f"Encode '{text3}': {encoded3}")
    print(f"Decode '{encoded3}': {decoded3}")
    print(f"Encode '{text4}': {encoded4}")
    print(f"Decode '{encoded4}': {decoded4}")