def run_length_encoding(input_string):
    if not input_string:
        return []
    
    result = []
    count = 1
    length = len(input_string)
    
    for i in range(1, length):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append((input_string[i - 1], count))
            count = 1
    
    result.append((input_string[-1], count))
    return result

if __name__ == '__main__':
    sample = "aaabbc"
    print(run_length_encoding(sample))