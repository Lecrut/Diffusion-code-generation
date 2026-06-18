def first_letters(s: str) -> str: 
    return " ".join(w[0] if w else "" for w in s.split()) 

if __name__ == '__main__': 
    print(first_letters("Hello World Python Programming"))