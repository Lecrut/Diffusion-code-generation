def categorize_text(text: str) -> str:
    category_map = {lambda x: 'Uppercase' if x.isupper() else None, lambda x: 'Lowercase' if x.islower() else None, lambda x: 'Titlecase' if x.istitle() else None, lambda x: 'Numeric' if x.isdigit() else None, lambda x: 'Alphanumeric' if x.isalnum() else None}
    for category in category_map:
        if category(text):
            return category(text)
    return 'Other'
if __name__ == '__main__':
    sample_text_1 = 'HELLO'
    sample_text_2 = 'hello'
    sample_text_3 = 'Hello'
    sample_text_4 = '123'
    sample_text_5 = 'abc123'
    print(categorize_text(sample_text_1))
    print(categorize_text(sample_text_2))
    print(categorize_text(sample_text_3))
    print(categorize_text(sample_text_4))
    print(categorize_text(sample_text_5))