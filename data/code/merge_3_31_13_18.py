class StringChecker:
    def check(self, text):
        """
        Determines if the input string is a palindrome after removing non-alphanumeric characters 
        and converting to lowercase.
        
        Args:
            text (str): The string to be checked.
            
        Returns:
            bool: True if 'text' is a palindrome, False otherwise.
        """
        filtered_text = ''.join(char.lower() for char in text if char.isalnum())
        return filtered_text == filtered_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()

    test_cases = [
        "A man, a plan, a canal: Panama",
        "race car",
        "",
        "Hello World!",
        "Was it a cat and I saw a bad?",
        "Madam in Eden, I'm Adam"
    ]

    for case in test_cases:
        result = checker.check(case)