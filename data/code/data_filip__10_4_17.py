def reverse_word_order(text):
    if not text or not text.strip():
        return ""
    words = text.split()
    words.reverse()
    return " ".join(words)

def _join_reversed(words):
    return " ".join(reversed(words))

def reverse_word_order_v2(text):
    words = text.split()
    return _join_reversed(words) if words else ""

if __name__ == "__main__":
    test_cases = [
        "The quick brown fox",
        "   Leading and trailing spaces   ",
        "Single",
        "",
        "a b c d e"
    ]
    for case in test_cases:
        output = reverse_word_order(case)
        print(output)