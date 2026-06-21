def total_length_of_strings(strings):
    def calculate_length(s):
        return len(s)
    
    total = 0
    for string in strings:
        total += calculate_length(string)
    return total

if __name__ == '__main__':
    sample_values = ["example", "testcase", "stringlength"]
    result = total_length_of_strings(sample_values)
    print(result)