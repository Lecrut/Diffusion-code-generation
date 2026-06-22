def reverse_string(input_string):
    if not input_string:
        return ""
    return input_string[::-1]

if __name__ == '__main__':
    sample_value = "Alibaba Cloud"
    result = reverse_string(sample_value)
    print(result)