def process_string(s):
    if not s:
        return (s, s, s)
    
    lowercased = s.lower()
    reversed_case = ''.join(c.swapcase() for c in s)
    
    return (s, lowercased, reversed_case)

if __name__ == '__main__':
    sample_input = "Python3.8"
    output = process_string(sample_input)
    print(output)