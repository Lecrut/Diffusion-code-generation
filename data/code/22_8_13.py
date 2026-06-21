import re

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "letmein",
    "football", "shadow", "simple", "michael", "ninja", "mustang", "password1",
    "access", "batman", "test", "pass", "god", "admin", "welcome", "login",
    "master", "hello", "charlie", "donald", "starwars", "passw0rd", "summer",
    "winter", "spring", "autumn", "love", "sex", "money", "power", "god",
    "angel", "devil", "angel1", "devil1", "love1", "hottie", "soccer", "hockey",
    "buddy", "buster", "ginger", "ranger", "buster", "ginger", "ginger", "ginger"
}

DICTIONARY_WORDS = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "her", "she", "an",
    "will", "my", "one", "all", "would", "there", "their", "what", "so",
    "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know",
    "take", "people", "into", "year", "your", "good", "some", "could",
    "them", "see", "other", "than", "then", "now", "look", "only", "come",
    "its", "over", "think", "also", "back", "after", "use", "two",
    "how", "our", "work", "first", "well", "way", "even", "new", "want",
    "because", "any", "these", "give", "day", "most", "us", "great",
    "between", "need", "large", "under", "never", "children", "small",
    "begin", "place", "here", "right", "still", "life", "hand", "high",
    "keep", "next", "child", "world", "show", "head", "old", "try",
    "house", "call", "school", "thing", "very", "next", "left", "own",
    "last", "long", "same", "tell", "low", "move", "home", "night",
    "light", "point", "face", "air", "war", "line", "change", "story",
    "run", "number", "part", "name", "man", "system", "problem", "fact"
}

def check_password_strength(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    lower_password = password.lower()
    if lower_password in COMMON_PASSWORDS:
        return False
    for word in DICTIONARY_WORDS:
        if word in lower_password:
            return False
    return True

if __name__ == '__main__':
    sample_passwords = [
        "short",
        "password",
        "StrongP@ss1",
        "12345678",
        "abcdefgh",
        "Complex#Pass99",
        "thequickbrownfox"
    ]
    results = [check_password_strength(p) for p in sample_passwords]
    print(results)