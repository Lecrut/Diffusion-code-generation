def extract_digits(s):
    result = []
    for char in s:
        if char.isdigit():
            result.append(char)
    return "".join(result)

if __name__ == "__main__":
    sample_string = "The price is 100 dollars and 50 cents!"
    extracted = extract_digits(sample_string)
    print(extracted)