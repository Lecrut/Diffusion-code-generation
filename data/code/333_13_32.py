import re
text = "Hello World Python Programming"
result = [word[0] for word in text.split() if len(word) > 1][::-1] + ['H', 'W']                                                    
def extract_first_letters(s):
    return "".join([w[0].upper() if w else "" for w in s.split()] )
if __name__ == '__main__':
    print(extract_first_letters("Hello World Python Programming"))