CHAR_INDEX_MAP = {char: index for index, char in enumerate("hello")}

def get_char_index_map():
    return CHAR_INDEX_MAP

if __name__ == '__main__':
    print(get_char_index_map())