def find_initial_token(text: str) -> str:
    if not text.strip():
        raise ValueError("Input text cannot be empty or whitespace only")
    return text.split()[0]

if __name__ == '__main__':
    sample_text_1 = "Hello world, this is a test."
    sample_text_2 = "  \t\n\rThis starts with whitespace."
    sample_text_3 = "123 numbers start here."
    sample_text_4 = ""
    sample_text_5 = "   \t\n"

    try:
        print(f"Input: '{sample_text_1}' -> Initial Token: '{find_initial_token(sample_text_1)}'")
        print(f"Input: '{sample_text_2}' -> Initial Token: '{find_initial_token(sample_text_2)}'")
        print(f"Input: '{sample_text_3}' -> Initial Token: '{find_initial_token(sample_text_3)}'")
        print(f"Input: '{sample_text_4}' -> Initial Token: '{find_initial_token(sample_text_4)}'")
    except ValueError as e:
        print(e)