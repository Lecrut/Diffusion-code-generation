import re
def find_initial_token(text: str) -> str:
    if not text:
        return ""
    match = re.match(r"(\S+)", text)
    if match:
        return match.group(1)
    return ""
if __name__ == '__main__':
    sample_text_1 = "This is a sample sentence."
    sample_text_2 = "  leading spaces before the first word."
    sample_text_3 = "123 numbers start here."
    sample_text_4 = ""
    sample_text_5 = "   \t\n\rFirst token test"
    print(f"Input: '{sample_text_1}' -> Initial Token: '{find_initial_token(sample_text_1)}'")
    print(f"Input: '{sample_text_2}' -> Initial Token: '{find_initial_token(sample_text_2)}'")
    print(f"Input: '{sample_text_3}' -> Initial Token: '{find_initial_token(sample_text_3)}'")
    print(f"Input: '{sample_text_4}' -> Initial Token: '{find_initial_token(sample_text_4)}'")
    print(f"Input: '{sample_text_5}' -> Initial Token: '{find_initial_token(sample_text_5)}'")