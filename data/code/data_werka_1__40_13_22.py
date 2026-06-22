def extract_first_alpha(s):
    for char in s:
        if char.isalpha():
            return char
    return None

if __name__ == '__main__':
    sample_values = ["123abc", "4567!@#def", "!@#$%^&*()", "GHI"]
    results = [extract_first_alpha(value) for value in sample_values]
    print(results)