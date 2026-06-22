import re

def run_length_encode(s):
    if not s:
        return []
    
    chunks = re.findall(r'(.)(\1*)', s)
    return [(char, 1 + len(counts)) for char, counts in chunks]

if __name__ == '__main__':
    print(run_length_encode('AAABBBCC'))