def total_length_of_strings(strings):
    def calculate_length(s):
        return len(s)
    
    return sum(calculate_length(s) for s in strings)

if __name__ == '__main__':
    sample_values = ["hello", "world", "this", "is", "a", "test"]
    result = total_length_of_strings(sample_values)
    print(result)