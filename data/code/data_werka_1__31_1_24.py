class StringUtils:

    def is_palindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        left, right = (0, len(filtered_chars) - 1)
        while left < right:
            if filtered_chars[left] != filtered_chars[right]:
                return False
            left += 1
            right -= 1
        return True
if __name__ == '__main__':
    utils = StringUtils()
    sample_strings = ['A man, a plan, a canal: Panama', 'racecar', 'hello']
    for s in sample_strings:
        print(f"'{s}' is a palindrome: {utils.is_palindrome(s)}")