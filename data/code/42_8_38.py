class StringJoiner:
    def __init__(self, separator=""):
        self.separator = separator

    def join(self, parts):
        if not isinstance(parts, list) or not all(isinstance(part, str) for part in parts):
            raise ValueError("Parts must be a list of strings.")
        return self.separator.join(parts)

def build_string(parts, separator=''):
    return StringJoiner(separator).join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "world", "this", "is", "a", "test"]
    separators = {
        "none": "",
        "space": " ",
        "comma": ",",
        "semicolon": ";"
    }
    for sep_name, sep_value in separators.items():
        result = build_string(sample_parts, separator=sep_value)
        print(f"Using '{sep_name}' separator: {result}")