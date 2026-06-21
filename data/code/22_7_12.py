import re

def decode_rle(compressed: str) -> str:
    def replace(match):
        char = match.group(2)
        count = int(match.group(1))
        return char * count
    return re.sub(r'(\d+)([a-zA-Z])', replace, compressed)

if __name__ == '__main__':
    result = decode_rle("2a3b1c")
    print(result)