def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_helper(substring):
        return substring[::-1]
    
    return reverse_helper(s)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)