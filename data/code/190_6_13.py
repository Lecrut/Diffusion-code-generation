KEY_SET = set()

def initialize_key_set(keys):
    global KEY_SET
    KEY_SET = set(keys)

def key_exists(key):
    return key in KEY_SET

if __name__ == '__main__':
    keys = ['apple', 'banana', 'cherry']
    initialize_key_set(keys)
    print(f"Key exists: {'apple' in KEY_SET}")
    print(f"Key exists: {'orange' in KEY_SET}")