def capitalize_first_letter_only(text: str) -> str:
    if not text:
        return ""
    result = list(text)
    result[0] = result[0].upper()
    return "".join(result[1:])
if __name__ == '__main__':
    sample_text_1 = "this is a sample sentence for testing"
    sample_text_2 = "another example text"
    sample_text_3 = ""
    sample_text_4 = "a"
    sample_text_5 = "already capitalized"
    print(f"Original: '{sample_text_1}'")
    print(f"Processed: '{capitalize_first_letter_only(sample_text_1)}'\n")
    print(f"Original: '{sample_text_2}'")
    print(f"Processed: '{capitalize_first_letter_only(sample_text_2)}'\n")
    print(f"Original: '{sample_text_3}'")
    print(f"Processed: '{capitalize_first_letter_only(sample_text_3)}'\n")
    print(f"Original: '{sample_text_4}'")
    print(f"Processed: '{capitalize_first_letter_only(sample_text_4)}'\n")
    print(f"Original: '{sample_text_5}'")
    print(f"Processed: '{capitalize_first_letter_only(sample_text_5)}'\n")