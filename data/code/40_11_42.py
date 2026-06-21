def get_first_letter(s):
    return s[0] if s else ""

if __name__ == '__main__':
    sample_values = ["Qwen", "", "AI", "Alibaba"]
    results = [get_first_letter(value) for value in sample_values]
    print(results)