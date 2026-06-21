def sort_strings_by_length(strings):
    if not strings:
        return []
    
    def length_key(s):
        return len(s)
    
    return sorted(strings, key=length_key)

if __name__ == '__main__':
    sample_input = ["blueberry", "strawberry", "raspberry", "blackberry", "a"]
    result = sort_strings_by_length(sample_input)
    print(result)