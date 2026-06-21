def run_length_encode(s):
    if not s:
        return []
    
    encoding = [
        (count, char) for char, count in 
        [
            (key, len(list(group))) 
            for key, group in __import__('itertools').groupby(s)
        ]
    ]
    
    return encoding

if __name__ == '__main__':
    input_string = "aabcccaaa"
    result = run_length_encode(input_string)
    print(result)