import itertools
import operator

def rle_encode(text: str) -> str:
    if not text:
        return ""
    
    def _format_group(key, group):
        count = len(list(group))
        if count == 1:
            return f"{key}"
        return f"{count}{key}"
    
    encoded_parts = [
        _format_group(key, group)
        for key, group in itertools.groupby(text)
    ]
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    test_string = "aaabbcddddddfff"
    result = rle_encode(test_string)
    print(result)