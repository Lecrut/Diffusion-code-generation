class DataSanitizer:
    DEFAULT_WHITESPACE = frozenset(' \t\n\r\x0b\x0c')

    def __init__(self, custom_whitespace=None):
        if custom_whitespace is None:
            self._chars = self.DEFAULT_WHITESPACE
        else:
            self._chars = frozenset(custom_whitespace)

    def sanitize(self, raw_data):
        if not isinstance(raw_data, str):
            return None
        
        left = 0
        length = len(raw_data)
        
        while left < length and raw_data[left] in self._chars:
            left += 1
            
        if left == length:
            return ""
            
        right = length - 1
        while right >= left and raw_data[right] in self._chars:
            right -= 1
            
        return raw_data[left : right + 1]

def format_report(label, value):
    return f"{label}: {repr(value)}"

if __name__ == '__main__':
    sanitizer = DataSanitizer()
    
    samples = [
        "  standard text  ",
        "\n\t  nested spaces  \t\n",
        "      ",
        "no_whitespace_here",
        404
    ]
    
    for item in samples:
        cleaned = sanitizer.sanitize(item)
        print(format_report("Result", cleaned))