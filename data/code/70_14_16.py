def get_first_last_chars(text):
    return (text[0], text[-1])

if __name__ == '__main__':
    sample_text = "example"
    first_char, last_char = get_first_last_chars(sample_text)
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")