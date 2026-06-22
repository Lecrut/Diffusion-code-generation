def clean_string(text):
    return ''.join(ch.lower() for ch in text if ch.isalnum())

def is_palindrome(s):
    cleaned = clean_string(s)
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = ["A man, a plan, a canal: Panama", "race a car", "No 'x' in Nixon"]
    for sample in samples:
        print(is_palindrome(sample))