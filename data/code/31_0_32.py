def is_palindrome(s: str) -> bool:
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    return filtered_chars == filtered_chars[::-1]
if __name__ == '__main__':
    sample_values = ['A man, a plan, a canal: Panama', 'race a car', ' ', "No 'x' in Nixon", 'Was it a car or a cat I saw?']
    for value in sample_values:
        print(is_palindrome(value))