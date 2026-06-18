def filter_alphanumeric(text):
    """
    Returns a string containing only alphanumeric characters from the input.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only alphanumeric characters, spaces and other 
             non-alphanumeric characters removed.
    """
    return ''.join(char for char in text if char.isalnum())

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [
        "Hello, World! 123",
        "!@#$%^&*()_+-=[]{}|;:,.<>? abc def ghi jkl mno pqr stu vwx yz zyx wvu tu s r q p o n m l k j i h g f e d c b a",
        "   Spaces everywhere 12345 !## $$$ %%%"
    ]

    for sample in samples:
        result = filter_alphanumeric(sample)
        print(f"Input: '{sample}'")
        print(f"Output: '{result}'")
        print("-" * 40)