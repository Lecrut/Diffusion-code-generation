class StringOperations:
    @classmethod
    def is_palindrome(cls, text):
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    sample_texts = ["A man, a plan, a canal: Panama", "racecar", "hello", "Was it a car or a cat I saw?"]
    for text in sample_texts:
        result = StringOperations.is_palindrome(text)
        print(f"'{text}' is a palindrome: {result}")