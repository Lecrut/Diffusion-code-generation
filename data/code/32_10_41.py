def validate_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

def string_length(s):
    validate_string(s)
    return len(s)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud Innovations"
    print(string_length(sample_string))