import itertools

def run_length_encode(text):
    if not text:
        return ""
    
    result = []
    for char, group in itertools.groupby(text):
        length = len(list(group))
        result.append(f"{char}{length}")
    
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode("aaabbc"))
    print(run_length_encode("abc"))
    print(run_length_encode(""))
    print(run_length_encode("aaaa"))