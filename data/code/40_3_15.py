def first_letters(s: str) -> str: return ' '.join(word[0].upper() if word else '' for word in s.split())
if __name__ == '__main__': print(first_letters("hello world python")) # Output: "H W P"
print(first_letters("   ")) # Output: ""