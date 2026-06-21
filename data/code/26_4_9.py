def run_length_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    generator = ((char, sum(1 for _ in group)) for char, group in __import__('itertools').groupby(input_string))
    
    for char, count in generator:
        if count > 1:
            result.append(f"{count}{char}")
        else:
            result.append(char)
            
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)