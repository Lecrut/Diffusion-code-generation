def check_string(input_str):
    return "apple" in input_str or "banana" in input_str or input_str.startswith("fruit")

if __name__ == '__main__':
    sample = "I have an apple and a banana."
    print(check_string(sample))