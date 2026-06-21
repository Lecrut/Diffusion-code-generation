KEY_TO_TOKEN = {
    "apple": "fruit1",
    "banana": "fruit2",
    "carrot": "vegetable1",
    "broccoli": "vegetable2"
}

def match_key_to_token(key):
    return KEY_TO_TOKEN.get(key, None)

if __name__ == '__main__':
    print(f"Matching 'apple': {match_key_to_token('apple')}")
    print(f"Matching 'banana': {match_key_to_token('banana')}")
    print(f"Matching 'grape': {match_key_to_token('grape')}")