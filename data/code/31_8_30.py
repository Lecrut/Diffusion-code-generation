class StringOperations:
    @classmethod
    def is_palindrome(cls, text):
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?"
    ]
    
    for value in sample_values:
        result = StringOperations.is_palindrome(value)
        print(f"'{value}' is a palindrome: {result}")