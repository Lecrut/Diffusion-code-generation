def is_valid_string(s):
    return isinstance(s, str)

def get_first_letter(s):
    if not is_valid_string(s) or not s:
        return ""
    return s[0]

if __name__ == '__main__':
    sample_values = ["Alibaba", "", "Cloud", "Qwen"]
    results = [get_first_letter(value) for value in sample_values]
    print(results)