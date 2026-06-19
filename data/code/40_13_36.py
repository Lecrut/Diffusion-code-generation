def get_first_alphabetic_character(s):
    try:
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        
        for char in s:
            if char.isalpha():
                return char
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    sample_strings = ["123abc456", "!!!hello", "no leading numbers", " ", "", 123, None]
    results = [get_first_alphabetic_character(s) for s in sample_strings]
    print(results)